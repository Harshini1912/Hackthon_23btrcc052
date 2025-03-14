import speech_recognition as sr
import pyttsx3
import pywhatkit as kit 
import os
import random
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()
def listen_to_user():
    """Listens for a command from the user."""
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return None
def process_command(command):
    """Processes the recognized voice command."""
    if "play some random music" in command:
        return "play_random_music"
    elif "open the calculator" in command:
        return "open_calculator"
    elif "open whatsapp" in command:
        return "open_whatsapp"
    else:
        return "unknown_command"
def perform_action(action):
    """Performs the action based on the command."""
    if action == "play_random_music":
        play_random_music() 
    elif action == "open_calculator":
        open_calculator()  
    elif action == "open_whatsapp":
        open_whatsapp() 
    else:
        speak("Sorry, I did not understand that command.")
        print("Action: Unknown command.")
def play_random_music():
    """"Plays random music from Youtube."""
    songs = [
        "I Wanna Be Yours",
        "Ra Ra Krishnayya",
        "Levitating",
        "Darlingey",
        "Stay with me"
    ]
    song = random.choice(songs)  
    print(f"Now playing: {song}")
    speak(f"Now playing {song} on Youtube.")
    kit.playonyt(song) 
def open_calculator():
    """Opens the calculator application."""
    print("Opening the calculator...")
    speak("Opening the calculator.")
    os.system("calc") 
def open_whatsapp():
    """Opens WhatsApp Web."""
    print("Opening WhatsApp...")
    speak("Opening WhatsApp.")
    kit.search("https://web.whatsapp.com") 
def main():
    """Main loop to continuously listen for commands."""
    while True:
        command = listen_to_user()
        if command:
            action = process_command(command)
            perform_action(action)
if __name__ == "__main__":
    main()
