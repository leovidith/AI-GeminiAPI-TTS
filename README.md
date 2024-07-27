# Voice Assistant with Gemini AI and Speech Recognition

This project is a simple voice assistant application using Python. It integrates the Gemini AI for generating responses and uses `pyttsx3` for text-to-speech functionality. The application supports both text input and audio input, with a graphical user interface (GUI) built using Tkinter.

## Features

- **Text Input**: Users can enter text directly and receive a spoken response.
- **Audio Input**: Users can use their microphone to input speech, which will be recognized and converted to text.
- **AI Responses**: Utilizes the Gemini AI to generate responses based on user input.
- **Text-to-Speech**: Converts AI-generated responses to speech using `pyttsx3`.
- **GUI**: User-friendly interface created with Tkinter for easy interaction.

## Requirements

- `Python 3.x`
- `pyttsx3`
- `speech_recognition`
- `google-generativeai`
- `tkinter`

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/voice-assistant.git
    cd voice-assistant
    ```

2. **Install the required packages**:
    ```bash
    pip install pyttsx3 speech_recognition google-generativeai tk
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Using the GUI**:
    - Enter your text in the provided input field and click "Submit Text" to get a response.
    - Click "Use Audio Input" to speak to the assistant and get a spoken response.

## Code Overview

### Main Functions

- `configure_genai(api_key)`: Configures the Gemini AI with the provided API key.
- `recognize_speech(recognizer)`: Captures audio from the microphone and converts it to text.
- `get_response(chat_session, text, imp)`: Sends the input text to the Gemini AI and gets the response.
- `speak_text(text)`: Converts the response text to speech.
- `create_gui()`: Creates and runs the Tkinter GUI for the application.

### Main Script

The main script initializes the GUI and sets up the necessary components for handling text and audio inputs.

```python
import pyttsx3 as tts
import speech_recognition as sr
import google.generativeai as genai
import tkinter as tk
from tkinter import messagebox

# Configuration and utility functions...

def main():
    create_gui()

if __name__ == "__main__":
    main()
```

Contribution
Contributions are welcome! Please create an issue or submit a pull request for any improvements or new features.

Acknowledgements
Thanks to Google Generative AI for providing the AI model.
Inspired by the need for simple and accessible voice assistant tools.
