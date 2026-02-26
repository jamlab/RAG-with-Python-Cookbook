import sys
import os

# Make app_helper_functions importable when running tests from this directory
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "11.1_and_11.2_streamlit_chatbot_apps",
    ),
)
