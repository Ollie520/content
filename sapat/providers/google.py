import os
from typing import Optional

from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account

from sapat.providers.base import Provider, TranscriptionResult

class GoogleProvider(Provider):
    """
    Google Cloud Speech-to-Text provider for audio transcription.
    """
    def __init__(self, credentials_path: Optional[str] = None):
        """
        Initializes the GoogleProvider.

        Args:
            credentials_path (Optional[str]): Path to the Google Cloud service account key file.
                                              If None, credentials will be loaded from GOOGLE_APPLICATION_CREDENTIALS
                                              environment variable or default ADC.
        """
        self.client = self._initialize_client(credentials_path)

    def _initialize_client(self, credentials_path: Optional[str]):
        """Initializes the Google Speech client with credentials."""
        if credentials_path:
            if not os.path.exists(credentials_path):
                raise FileNotFoundError(f"Google credentials file not found at: {credentials_path}")
            credentials = service_account.Credentials.from_service_account_file(credentials_path)
            return speech.SpeechClient(credentials=credentials)
        else:
            # Use default application credentials (e.g., GOOGLE_APPLICATION_CREDENTIALS env var)
            return speech.SpeechClient()

    def transcribe(self, audio_file_path: str, language: str = "en-US") -> TranscriptionResult:
        """
        Transcribes an audio file using Google Cloud Speech-to-Text.

        Args:
            audio_file_path (str): Path to the audio file.
            language (str): The language of the audio (e.g., "en-US", "es-ES").

        Returns:
            TranscriptionResult: An object containing the transcribed text and other metadata.
        """
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Audio file not found at: {audio_file_path}")

        with open(audio_file_path, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, # Assuming common audio format, can be auto-detected
            sample_rate_hertz=16000, # Common sample rate, ideally should be detected or configurable
            language_code=language,
            enable_automatic_punctuation=True,
        )

        print(f"Transcribing '{audio_file_path}' using Google Cloud Speech-to-Text...")
        response = self.client.recognize(config=config, audio=audio)

        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript + " "

        return TranscriptionResult(
            provider="google",
            language=language,
            text=transcript.strip(),
            raw_response=response.to_json(),
        )

