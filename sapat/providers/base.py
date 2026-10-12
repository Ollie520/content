from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

class ProviderName(Enum):
    OPENAI = "openai"
    GROQ = "groq"
    WHISPER = "whisper"
    GOOGLE = "google" # Add new provider to enum

@dataclass
class TranscriptionResult:
    provider: str
    language: str
    text: str
    raw_response: dict # Store the raw response from the API for debugging/advanced use

class Provider(ABC):
    @abstractmethod
    def transcribe(self, audio_file_path: str, language: str) -> TranscriptionResult:
        pass

