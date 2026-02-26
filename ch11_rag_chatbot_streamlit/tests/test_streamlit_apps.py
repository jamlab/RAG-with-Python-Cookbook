"""
Tests for the ch11 streamlit chatbot applications.

Runs using streamlit's AppTest framework so no browser is required.
"""

import os
from unittest.mock import patch

import pytest
from streamlit.testing.v1 import AppTest

APP_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "11.1_and_11.2_streamlit_chatbot_apps",
)


def app_path(filename):
    return os.path.join(APP_DIR, filename)


def make_app(filename):
    """Return a freshly initialised and run AppTest for *filename*."""
    at = AppTest.from_file(app_path(filename))
    at.run()
    return at


# ---------------------------------------------------------------------------
# App 01 – most_basic_rag_app
# ---------------------------------------------------------------------------


@pytest.fixture
def app01():
    return make_app("01_most_basic_rag_app.py")


class TestApp01MostBasic:
    def test_app_loads_without_error(self, app01):
        assert not app01.exception

    def test_title(self, app01):
        assert app01.title[0].value == "Simple Chatbot"

    def test_text_input_present(self, app01):
        assert len(app01.text_input) == 1
        assert app01.text_input[0].label == "You:"

    def test_bot_echoes_user_input(self, app01):
        app01.text_input[0].input("Hello").run()
        assert not app01.exception
        assert any("You said 'Hello'" in m.value for m in app01.markdown)


# ---------------------------------------------------------------------------
# App 02 – simple_rag_app (static chat messages)
# ---------------------------------------------------------------------------


@pytest.fixture
def app02():
    return make_app("02_simple_rag_app.py")


class TestApp02SimpleRagApp:
    def test_app_loads_without_error(self, app02):
        assert not app02.exception

    def test_two_chat_messages_displayed(self, app02):
        assert len(app02.chat_message) == 2

    def test_user_message_role(self, app02):
        assert app02.chat_message[0].name == "user"

    def test_assistant_message_role(self, app02):
        assert app02.chat_message[1].name == "assistant"


# ---------------------------------------------------------------------------
# App 03 – simple_rag_app_2 (interactive chatbot with keyword logic)
# ---------------------------------------------------------------------------


@pytest.fixture
def app03():
    return make_app("03_simple_rag_app_2.py")


class TestApp03SimpleRagApp2:
    def test_app_loads_without_error(self, app03):
        assert not app03.exception

    def test_title(self, app03):
        assert app03.title[0].value == "Simple RAG Chat App"

    def test_chat_input_present(self, app03):
        assert len(app03.chat_input) == 1

    def test_hello_response(self, app03):
        app03.chat_input[0].set_value("hello").run()
        assert not app03.exception
        assistant_msgs = [cm for cm in app03.chat_message if cm.name == "assistant"]
        assert len(assistant_msgs) == 1
        assert "Hello" in assistant_msgs[0].markdown[0].value

    def test_rag_response(self, app03):
        app03.chat_input[0].set_value("What is RAG?").run()
        assert not app03.exception
        assistant_msgs = [cm for cm in app03.chat_message if cm.name == "assistant"]
        assert len(assistant_msgs) == 1
        assert "RAG" in assistant_msgs[0].markdown[0].value

    def test_default_response(self, app03):
        app03.chat_input[0].set_value("Tell me something").run()
        assert not app03.exception
        assistant_msgs = [cm for cm in app03.chat_message if cm.name == "assistant"]
        assert len(assistant_msgs) == 1
        assert "Tell me something" in assistant_msgs[0].markdown[0].value

    def test_user_message_preserved(self, app03):
        app03.chat_input[0].set_value("hello").run()
        user_msgs = [cm for cm in app03.chat_message if cm.name == "user"]
        assert len(user_msgs) == 1
        assert user_msgs[0].markdown[0].value == "hello"


# ---------------------------------------------------------------------------
# App 04 – simple_rag_app_3 (full RAG pipeline, external APIs mocked)
# ---------------------------------------------------------------------------


@pytest.fixture
def app04():
    return make_app("04_simple_rag_app_3.py")


class TestApp04SimpleRagApp3:
    def test_app_loads_without_error(self, app04):
        assert not app04.exception

    def test_title(self, app04):
        assert app04.title[0].value == "My Streamlit RAG App"

    def test_chat_input_present(self, app04):
        assert len(app04.chat_input) == 1

    def test_chat_response_with_mocked_apis(self, app04):
        """Full conversation turn with all external calls mocked."""
        mock_weather = {
            "current": {
                "temperature_2m": 18.5,
                "relative_humidity_2m": 60,
                "wind_speed_10m": 12,
            }
        }

        with patch(
            "app_helper_functions.extract_the_city_and_country",
            return_value={"city": "Paris", "country": "France"},
        ), patch(
            "app_helper_functions.get_coordinates_for_city",
            return_value=(48.8566, 2.3522),
        ), patch(
            "app_helper_functions.get_current_weather_open_meteo",
            return_value=mock_weather,
        ), patch(
            "app_helper_functions.send_prompt_to_llm",
            return_value="It is 18.5°C in Paris with 60% humidity.",
        ):
            app04.chat_input[0].set_value(
                "What is the weather in Paris, France?"
            ).run()

        assert not app04.exception
        assert len(app04.chat_message) == 2
        user_msgs = [cm for cm in app04.chat_message if cm.name == "user"]
        assistant_msgs = [cm for cm in app04.chat_message if cm.name == "assistant"]
        assert user_msgs[0].markdown[0].value == "What is the weather in Paris, France?"
        assert "18.5" in assistant_msgs[0].markdown[0].value
