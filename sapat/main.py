from typing import Optional

from sapat.providers.base import ProviderName, TranscriptionResult
from sapat.providers.openai import OpenAIProvider
from sapat.providers.groq import GroqProvider
from sapat.providers.whisper import WhisperProvider
from sapat.providers.google import GoogleProvider # Import the new provider

def transcribe_audio(
    audio_file_path: str,
    provider_name: ProviderName,
    api_key: Optional[str] = None,
    google_credentials_path: Optional[str] = None, # New argument
    language: str = "en",
    whisper_model: str = "base",
) -> TranscriptionResult:
    """
    Transcribes an audio file using the specified provider.

    Args:
        audio_file_path (str): Path to the audio file.
        provider_name (ProviderName): The transcription provider to use.
        api_key (Optional[str]): API key for OpenAI or Groq.
        google_credentials_path (Optional[str]): Path to Google Cloud service account key file.
        language (str): Language of the audio.
        whisper_model (str): Model size for local Whisper transcription.

    Returns:
        TranscriptionResult: The result of the transcription.
    """
    provider = None
    if provider_name == ProviderName.OPENAI:
        if not api_key:
            raise ValueError("OpenAI API key is required for OpenAI provider.")
        provider = OpenAIProvider(api_key=api_key)
    elif provider_name == ProviderName.GROQ:
        if not api_key:
            raise ValueError("Groq API key is required for Groq provider.")
        provider = GroqProvider(api_key=api_key)
    elif provider_name == ProviderName.WHISPER:
        provider = WhisperProvider(model_size=whisper_model)
    elif provider_name == ProviderName.GOOGLE: # Instantiate the new provider
        provider = GoogleProvider(credentials_path=google_credentials_path)
    else:
        raise ValueError(f"Unsupported provider: {provider_name}")

    return provider.transcribe(audio_file_path, language)

