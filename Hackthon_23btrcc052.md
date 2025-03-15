AI-Powered Voice Assistant

This project implements a simple AI-powered voice assistant using Python, allowing users to give voice commands for tasks like playing music, opening the calculator, and opening WhatsApp. The assistant uses speech recognition, text-to-speech, and web automation to perform tasks based on voice input.

Features

Voice Command Recognition: Listens for user commands and converts speech to text.
Text-to-Speech (TTS): Provides verbal feedback to the user.
Music Playback: Plays a random song from YouTube using pywhatkit.
Open Applications: Opens the calculator application on the system and WhatsApp Web.
Real-time Interaction: Continuously listens for commands in an infinite loop.

Technologies Used
Speech Recognition: speech_recognition library for converting speech to text.
Text-to-Speech (TTS): pyttsx3 library for converting text to speech.
Web Automation: pywhatkit library for performing actions like playing music on YouTube and searching URLs.
Operating System Interactions: os library to open system applications like the calculator.

Installation

(1)Clone the repository
(2)Install required dependencies
(3)Install PyAudio (required for microphone input with SpeechRecognition)
(4)Run the assistant

How it Works

Speech Recognition: The assistant uses the speech_recognition library to listen to the user's voice and convert the spoken words into text.
Command Processing: After the voice command is recognized, the process_command function checks if the command matches one of the predefined actions like playing music, opening the calculator, or opening WhatsApp Web.
Text-to-Speech: The assistant provides verbal feedback using pyttsx3 based on the action being performed. For example, it will say, "Now playing [song name]" when it plays music or "Opening WhatsApp" when opening WhatsApp Web.

Performing Actions

Play Random Music: The assistant picks a random song from a predefined list and uses pywhatkit to play it on YouTube.
Open Calculator: The assistant opens the system calculator using os.system("calc").
Open WhatsApp: The assistant opens WhatsApp Web by searching for "https://web.whatsapp.com" using pywhatkit.

Example Commands

"Play some random music": The assistant will randomly pick a song from the list and play it on YouTube.
"Open the calculator": The assistant will open the calculator application on your computer.
"Open WhatsApp": The assistant will open WhatsApp Web in the default browser.

Acknowledgments

SpeechRecognition library for speech-to-text conversion.
pyttsx3 for text-to-speech functionality.
pywhatkit for interacting with YouTube and opening URLs.
The Python community for maintaining and contributing to these libraries.
