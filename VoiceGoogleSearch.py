import speech_recognition as sr
import webbrowser

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to perform actions based on commands
def perform_action(command):
    if "open Google" in command:
        webbrowser.open("https://www.google.com")
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
    # Add more actions here based on recognized commands
    else:
        print("Command not recognized.")

# Function to listen to voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        recognized_text = recognizer.recognize_google(audio)
        print(f"You said: {recognized_text}")
        return recognized_text.lower()  # Convert recognized text to lowercase
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""

# Main loop for continuous listening
while True:
    command = listen()
    if "exit" in command:
        print("Exiting...")
        break
    else:
        perform_action(command)
