import pyttsx3
import datetime
import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import time

# Initialize the speech engine
engine = pyttsx3.init()

# Set the current voice to Jarvis
currentVoice = "Jarvis"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getVoices(voice):
    global currentVoice
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        currentVoice = "Jarvis"
        speak(f"Hello, This is {currentVoice}")
    elif voice == 2:
        engine.setProperty('voice', voices[1].id)
        currentVoice = "Friday"
        speak(f"Hello, This is {currentVoice}")

def time_():
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    root.after(1000, time_) 

def date_():
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    date_label.config(text=current_date)

def greeting():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    elif 18 <= hour < 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")

def wishMe():
    speak("Welcome back Sir!")
    greeting()
    speak(f"{currentVoice} at your service, how can I help?")
    output_text.insert(tk.END, f"{currentVoice} at your service.\n")

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(query)
        output_text.insert(tk.END, f"Command: {query}\n")
    except Exception as e:
        print(e)
        speak("Sorry, can you repeat that again?")
        output_text.insert(tk.END, "Error: Sorry, can you repeat again...\n")
        return None
    return query

def executeCommand():
    query = takeCommandMic().lower()
    if query:
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'change voice' in query or 'change your voice' in query:
            if currentVoice == "Jarvis":
                getVoices(2)
            else:
                getVoices(1)
        elif 'quit' in query or 'exit' in query:
            speak(f"{currentVoice} out!")
            root.quit()

root = tk.Tk()
root.title("Jarvis AI")
root.geometry("800x600")
root.config(bg='black')

date_label = tk.Label(root, text="", font=("Arial", 12), fg="cyan", bg="black")
date_label.place(x=10, y=10)

time_label = tk.Label(root, text="", font=("Arial", 12), fg="cyan", bg="black")
time_label.place(x=10, y=30)

logo_image = Image.open("jarvish.jpg") 
logo_image = logo_image.resize((320, 180))  
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg="black")
logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

output_text = scrolledtext.ScrolledText(root, width=40, height=5, wrap=tk.WORD, bg="black", fg="cyan", font=("Arial", 12))
output_text.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

mic_button = tk.Button(root, text="Activate", command=executeCommand, font=("Arial", 14), bg="cyan", fg="black")
mic_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

date_()
time_()

root.mainloop()