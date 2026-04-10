import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def jarvis():
    speak("Hello, I am Jarvis. How can I help you?")
    while True:
        command = listen()
        if 'wikipedia' in command:
            speak("Searching Wikipedia...")
            query = command.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except Exception:
                speak("Sorry, I couldn't find anything.")
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        elif 'hello' in command:
            speak("Hello! Nice to talk to you.")
        else:
            speak("I am still learning. Please try another command.")

if __name__ == "__main__":
    jarvis()