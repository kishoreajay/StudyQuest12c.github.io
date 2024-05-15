import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusting for ambient noise
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except Exception as e:
        print("Error:", str(e))
        return None

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Opens the generated audio file
    # On macOS, you can use the following line instead:
    # os.system("afplay output.mp3")

def translate_text(text, dest_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language)
    return translated_text.text

def main():
    print("Choose an option:")
    print("1. Translate text")
    print("2. Convert speech to text")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        text = input("Enter the text to translate: ")
        dest_language = input("Enter the destination language (e.g., 'fr' for French): ")
        translated_text = translate_text(text, dest_language)
        print("Translated text:", translated_text)
        text_to_speech(translated_text, dest_language)
    elif choice == '2':
        text = speech_to_text()
        if text:
            print("Converted text:", text)
            text_to_speech(text)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
