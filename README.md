# SAPAT: Simple Audio Processing And Transcription

SAPAT (Simple Audio Processing And Transcription) is a command-line tool designed to make audio transcription easy and flexible. It supports multiple transcription providers, allowing you to switch between them with a single command.

## Features

*   **Multiple Providers**: Transcribe audio using OpenAI Whisper API, Groq API, local Whisper models, and Google Cloud Speech-to-Text.
*   **Easy CLI**: Simple command-line interface for quick transcriptions.
*   **Language Support**: Specify the language for transcription.
*   **Output to File**: Save transcriptions directly to a text file.

## Supported Providers

*   **OpenAI Whisper API**: Utilizes OpenAI's powerful Whisper models via their API.
*   **Groq API**: Leverages Groq's fast inference engine for transcription (often using Whisper models).
*   **Local Whisper**: Transcribe audio offline using local Whisper models (requires `whisper-timestamped`).
*   **Google Cloud Speech-to-Text**: Integrates with Google's robust cloud-based speech recognition service.

## Installation

1.  **Clone the repository:**
    