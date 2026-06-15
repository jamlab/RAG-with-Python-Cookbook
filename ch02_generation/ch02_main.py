from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)
# Nur die Resource-Basis, OHNE /openai/v1
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT").split("/openai")[0]

audio_path = "../datasets/audio_files/harvard.wav"

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=endpoint,                 # https://<resource>.openai.azure.com
    api_version="2025-03-01-preview",        # Audio-fähige Preview-Version (oder neuer)
)

with open(audio_path, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="gpt-4o-transcribe",           # = Deployment-Name
        file=audio_file,
    )

print(transcript.text)