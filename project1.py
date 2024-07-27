import pyttsx3 as tts
import speech_recognition as sr
import google.generativeai as genai
import requests

def configure_genai(api_key):
    genai.configure(api_key=api_key)

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    return chat_session

def recognize_speech(recognizer):
    with sr.Microphone() as source:
        try:
            print("Please say something")
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            print("Recognizing...")
            text = recognizer.recognize_google(audio_data)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection")
            return ""

def get_response(chat_session, text, imp):
    if text:
        response = chat_session.send_message(text + imp)
        response_text = response.candidates[0].content if response.candidates else "No response from AI"
        return response_text
    return ""

def speak_text(text):
    engine = tts.init()
    engine.say(text)
    engine.runAndWait()

def get_weather(api_key, city):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"  # No air quality index data
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['current']['condition']['text']
        temp = data['current']['temp_c']
        weather_info = f"The weather in {city} is currently {weather} with a temperature of {temp}°C."
        return weather_info
    else:
        return "Could not retrieve weather information."

def main():
    genai_api_key = "geminiapikey"
    weather_api_key = "weatherapikey"
    imp = ": just respond with a plain text not like a markdown file also without any escape sequences"

    recognizer = sr.Recognizer()
    chat_session = configure_genai(genai_api_key)

    choice = input("Enter 1 for text input or 0 for audio input: ")

    if choice == '1':
        text = input("Please enter your text: ")
    elif choice == '0':
        text = recognize_speech(recognizer)
    else:
        print("Invalid choice")
        return

    if 'weather' in text.lower():
        city = input("Enter the city name for weather update: ")
        response_text = get_weather(weather_api_key, city)
        print(f"Weather: {response_text}")
        speak_text(response_text)
    elif text:
        response_text = get_response(chat_session, text, imp)
        print(f"Gemini: {response_text}")
        speak_text(response_text)
    else:
        print("No input provided.")

if __name__ == "__main__":
    main()
