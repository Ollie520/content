import argparse
import os
from typing import Optional

from sapat.main import transcribe_audio
from sapat.providers.base import ProviderName

def main():
    parser = argparse.ArgumentParser(
        description="Simple Audio Processing And Transcription (SAPAT) CLI."
    )
    parser.add_argument(
        "audio_file", type=str, help="Path to the audio file to transcribe."
    )
    parser.add_argument(
        "--provider",
        type=str,
        choices=[p.value for p in ProviderName],
        default=ProviderName.OPENAI.value,
        help="Transcription provider to use.",
    )
    parser.add_argument(
        "--language",
        type=str,
        default="en",
        help="Language of the audio (e.g., 'en' for OpenAI/Groq/Whisper, 'en-US' for Google).",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Optional path to save the transcription to a text file.",
    )
    parser.add_argument(
        "--openai-api-key",
        type=str,
        default=os.environ.get("OPENAI_API_KEY"),
        help="OpenAI API key. Defaults to OPENAI_API_KEY environment variable.",
    )
    parser.add_argument(
        "--groq-api-key",
        type=str,
        default=os.environ.get("GROQ_API_KEY"),
        help="Groq API key. Defaults to GROQ_API_KEY environment variable.",
    )
    parser.add_argument(
        "--google-credentials-path",
        type=str,
        default=os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"),
        help="Path to Google Cloud service account key file. Defaults to GOOGLE_APPLICATION_CREDENTIALS environment variable.",
    )
    parser.add_argument(
        "--whisper-model",
        type=str,
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size to use for local transcription.",
    )

    args = parser.parse_args()

    # Provider-specific key validation
    api_key: Optional[str] = None
    google_credentials_path: Optional[str] = None

    if args.provider == ProviderName.OPENAI.value:
        api_key = args.openai_api_key
        if not api_key:
            print("Error: OpenAI API key not provided. Set OPENAI_API_KEY environment variable or use --openai-api-key.")
            exit(1)
    elif args.provider == ProviderName.GROQ.value:
        api_key = args.groq_api_key
        if not api_key:
            print("Error: Groq API key not provided. Set GROQ_API_KEY environment variable or use --groq-api-key.")
            exit(1)
    elif args.provider == ProviderName.GOOGLE.value:
        google_credentials_path = args.google_credentials_path
        # GoogleProvider handles default ADC, so explicit check for path is only if user provided it
        # and it doesn't exist. If not provided, it will try default ADC.
        if google_credentials_path and not os.path.exists(google_credentials_path):
            print(f"Error: Google credentials file not found at '{google_credentials_path}'.")
            exit(1)
    elif args.provider == ProviderName.WHISPER.value:
        # No API key needed for local whisper
        pass
    else:
        print(f"Error: Unknown provider '{args.provider}'.")
        exit(1)

    try:
        result = transcribe_audio(
            audio_file_path=args.audio_file,
            provider_name=ProviderName(args.provider),
            api_key=api_key,
            google_credentials_path=google_credentials_path,
            language=args.language,
            whisper_model=args.whisper_model,
        )
        print("\n--- Transcription Result ---")
        print(f"Provider: {result.provider}")
        print(f"Language: {result.language}")
        print(f"Text:\n{result.text}")

        if args.output:
            with open(args.output, "w") as f:
                f.write(result.text)
            print(f"\nTranscription saved to: {args.output}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()

