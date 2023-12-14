import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
text_to_speech = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that. Can you please repeat?")
        return listen()
    except sr.RequestError as e:
        speak(f"Error fetching results from Google Speech Recognition: {e}")
        return None

# Function to handle user commands
def process_command(command):
    if "hello" in command:
        speak("Hello! This is Jarvis, How can I help you today?")
    elif "Dismissed" in command:
        speak("Sure! Have a great day, bye.")
        exit()
    elif "browse" in command:
        speak("Sure! What do you want to search for?")
        search_query = listen()
        if search_query:
            url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
            speak("Searching, please wait...")
            print("Searching, please wait...")
            webbrowser.open(url)
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "files" in command:
        speak("Sure! What file do you want to open?")
        file_name = listen()
        if file_name:
            try:
                os.startfile(file_name)  # Open file with default associated program
                speak("Opening the requested file...")
                print("Opening the requested file...")
            except FileNotFoundError:
                speak(f"Sorry, I couldn't find the file {file_name}")
    elif "open" in command and "application" in command:
        speak("Sure! What application do you want to open?")
        app_name = listen()
        if app_name:
            try:
                # Provide the full path to the application executable
                app_path = f"C:\\Path\\To\\{app_name}.exe"  # Replace with the actual path
                speak("Opening the requested app...")
                print("Opening the requested app...")
                os.startfile(app_path)
            except Exception as e:
                speak(f"Error opening the application, pardon")
    else:
        speak("I'm sorry, I didn't understand that. please repeat again")

# Main loop
if __name__ == "__main__":
    speak("Hello! I'm Jarvis, your virtual assistant. How can I assist you today?")

    while True:
        user_input = listen()

        if user_input:
            process_command(user_input)
