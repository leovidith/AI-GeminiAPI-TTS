import pyttsx3 as tts
import speech_recognition as sr
import google.generativeai as genai
import tkinter as tk
from tkinter import messagebox

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
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'female' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

def create_gui():
    api_key = "AIzaSyD2gAZda_jJnnm9NVkOhA1ty0GGDjy0CII"
    imp = ": just respond with a plain text not like a markdown file also without any escape sequences"

    recognizer = sr.Recognizer()
    chat_session = configure_genai(api_key)

    def on_submit():
        user_text = entry.get()
        response_text = get_response(chat_session, user_text, imp)
        messagebox.showinfo("Gemini", response_text)
        root.after(100, lambda: speak_text(response_text))

    def on_audio_input():
        text = recognize_speech(recognizer)
        if text:
            response_text = get_response(chat_session, text, imp)
            messagebox.showinfo("Gemini", response_text)
            root.after(100, lambda: speak_text(response_text))
        else:
            messagebox.showinfo("Gemini", "No input provided.")

    root = tk.Tk()
    root.title("Voice Assistant")

    label = tk.Label(root, text="Enter your text:")
    label.pack()

    entry = tk.Entry(root, width=50)
    entry.pack()

    submit_button = tk.Button(root, text="Submit Text", command=on_submit)
    submit_button.pack()

    audio_button = tk.Button(root, text="Use Audio Input", command=on_audio_input)
    audio_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
