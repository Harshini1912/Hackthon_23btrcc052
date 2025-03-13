import speech_recognition as sr
import pyttsx3
def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source, duration=2)  
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)  
        print(f"Recognized command: {command}")  
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return None
def process_command(command):
    if command and "lights" in command and "on" in command:
        return "turn_on_lights"
    elif command and "lights" in command and "off" in command:
        return "turn_off_lights"
    elif command and "temperature" in command and "set" in command:
        try:
            temp = int(command.split()[-2]) 
            return f"set_temperature_to_{temp}"
        except ValueError:
            return "Invalid temperature value."
    elif command and "weather" in command:
        return "get_weather"
    elif command and "play" in command and "music" in command:
        return "play_music"
    else:
        return "unknown_command"
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def main():
    while True:
        command = listen_to_user()
        if command:
            action = process_command(command)
            if action == "turn_on_lights":
                speak("Turning on the lights.")
                print("Action: Turning on the lights.")
            elif action == "turn_off_lights":
                speak("Turning off the lights.")
                print("Action: Turning off the lights.")
            elif "set_temperature_to_" in action:
                temp = action.split('_')[-1]
                speak(f"Setting temperature to {temp} degrees.")
                print(f"Action: Setting temperature to {temp} degrees.")
            elif action == "get_weather":
                speak("Getting the weather.")
                print("Action: Getting the weather.")
            elif action == "play_music":
                speak("Playing music.")
                print("Action: Playing music.")
            else:
                speak("Sorry, I did not understand that command.")
                print("Action: Unknown command.")
        else:
            print("No command detected.")
            speak("Please say something.")
if __name__ == "__main__":
    main()
