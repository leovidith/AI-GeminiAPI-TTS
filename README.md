# Voice Assistant with Weather Updates

This project implements a voice assistant that can process text and audio inputs to provide responses from a generative AI model. Additionally, it can fetch weather updates based on user input. The project uses the following technologies:

- **Google Generative AI** for generating responses.
- **Speech Recognition** for converting speech to text.
- **pyttsx3** for text-to-speech functionality.
- **WeatherAPI** for fetching weather information.

## Features

- **Text Input**: Allows users to enter text and receive a generated response.
- **Audio Input**: Converts spoken words into text and processes it to generate responses.
- **Weather Updates**: Provides current weather information based on user-specified city.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/Voice-Assistant-with-Weather-Updates.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Voice-Assistant-with-Weather-Updates
    ```

3. **Install the required packages:**

    Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    Install dependencies:

    ```bash
    pip install pyttsx3 SpeechRecognition google-generativeai requests
    ```

## Configuration

Update the following variables in `main.py`:

- **`genai_api_key`**: Replace with your API key for Google Generative AI.
- **`weather_api_key`**: Replace with your API key for WeatherAPI.

## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **Select Input Method:**

    - **Enter `1`** to input text manually.
    - **Enter `0`** to use audio input.

3. **Weather Updates:**

    - If you mention the term "weather" in your input, the program will ask for a city name and fetch the current weather information for that city.

## Example

### Text Input

```plaintext
Enter 1 for text input or 0 for audio input: 1
Please enter your text: What is the weather in London?
Weather: The weather in London is currently Clear with a temperature of 15°C.
