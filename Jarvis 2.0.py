import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from credentials import senderEmail, ePWD
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import psutil
from nltk.tokenize import word_tokenize
import google.generativeai as genai
from geminiAPI import apiKey

genai.configure(api_key=apiKey)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how Gemini API Works!")


engine = pyttsx3.init()

currentVoice = "Jarvis"
currentName = "Swapnil"
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getVoices(voice):
    global currentVoice
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice',voices[1].id)
        currentVoice =  "Jarvis"
        speak(f"Hello, This is {currentVoice}")
    elif voice == 2:
        engine.setProperty('voice',voices[2].id)
        currentVoice = "Friday"
        speak(f"Hello, This is {currentVoice}")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current Time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The Current Date is:")
    speak(year)
    speak(month)
    speak(day)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak(f"Good Morning {currentName}")
    elif hour >=12 and hour<18:
        speak(f"Good afternoon {currentName}")
    elif hour >=18 and hour < 24:
        speak(f"Good evening {currentName}")
    else:
        speak(f"Good Night {currentName}")

def wishMe():
    speak(f"Welcome {currentName}!")
    greeting()
    speak(f"{currentVoice} at your service, how can i help?")

def sendEmail(receiver ,subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail,ePWD)  
    email = EmailMessage()
    email['From'] = senderEmail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.close()

def sendWhatsAppMsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchGoogle():
    speak(f"What can I Google For You?")
    search = takeCommandMic()
    wb.open(f'https://www.google.com/search?q={search}')

def playYT():
    speak("What Should i Play for you on YouTube?")
    topic = takeCommandMic()
    pywhatkit.playonyt(topic)

def weatherCall():
    city = "Kathmandu"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=7a0998e42239a0a1fc3670f211be83ae"
    res = requests.get(url)
    data = res.json()

    weather = data['weather'][0]['main']
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    feels_like = round((feels_like - 32) * 5/9)
    temperature = round((temperature - 32) * 5/9)
    description = data['weather'][0]['description']

    speak(f"Weather in {city} is like:")
    speak(f"The Temperature is {temperature} degree Celcius but it feels like {feels_like} degree Celcius")
    speak(f"The Weather is {weather}")
    speak(f"So There is {description}")

def news():
    newsapi = NewsApiClient(api_key='9fc337d72e1c4b919f905b272ddf4fce')

    speak("What topic do you need the news about?")
    topic = takeCommandMic()
    data = newsapi.get_everything(q=topic,language='en',page_size=5)

    newsData = data['articles']
    for i,j in enumerate(newsData):
        print(f'{i}{j["description"]}')
        speak(f'{i}{j["description"]}')

    speak("That is it for now , I will keep you updated with the latest news")

def textToSpeech():
    text = clipboard.paste()
    print(text)
    speak(text)

def openVS():
    path = 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
    os.startfile(path)

def openEdge():
    path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
    os.startfile(path)

def sayJokes():
    speak("Here is a joke for you")
    speak(pyjokes.get_joke())

def screenshot():
    name_img = tt.time()
    name_img = f'D:\\Python Projects\\J.A.R.V.I.S\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def rememberThings():
    speak("What should I remember?")
    data = takeCommandMic()
    speak(f"You said to  remember that: {data}")
    remember = open('data.txt','w')
    remember.write(data)
    remember.close()

def readRemembered():
    remember = open('data.txt','r')
    speak(f"You said to remember that: {remember.read()}")

def passwordGenerator():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    speak("Please enter the length of the password you want to generate:")
    passwordLength = int(input("Enter the length of the passowrd you want to generate:"))
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)

    random.shuffle(s)
    newPassword = ("".join(s[0:passwordLength]))
    print(newPassword)
    speak(newPassword)

def flipCoin():
    speak("Flipping a Coin now!")
    coin = ['heads','tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak(f"I flipped the coin and got {toss}")

def rollDice():
    speak("Rolling a Dice now!")
    die =  ['1','2','3','4','5','6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak(f"I rolled the dice and got {roll}")

def cpuUsage():
    speak("Checking CPU usage now!")
    usage = str(psutil.cpu_percent())
    speak(f"CPU usage is {usage}%")
    battery  = psutil.sensors_battery()
    speak(f"System battery is at {battery.percent}%")

def takeCommandCMD():
    query = input("How can i help?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry, can you repeat again...")
    return query

if __name__ == "__main__":
    wishMe()
    flag = True
    wakeWord = "jarvis"
    print(response.text)
    while flag:
        query = takeCommandMic().lower()
        query = word_tokenize(query)

        if wakeWord in query:
            if 'time' in query:
                time()
            
            elif 'date' in query:
                date()
            
            elif 'change voice' in query or 'change your voice' in query or 'change to' in query:
                if currentVoice == "Jarvis":
                    getVoices(2)
                else:
                    getVoices(1)
            
            elif 'send email' in query or 'sending a mail' in query:
                try:
                    speak("Please enter the email of the person you want to mail")
                    receiver = input("Please Enter the E-mail of the Person You Want to Mail:\n")
                    speak("Enter the Subject of message")
                    subject = takeCommandMic()
                    speak("Enter the Message you want to send")
                    message = takeCommandMic()
                    sendEmail(receiver, subject, message)
                    speak("Email Sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry, cannot send your email!")    
            
            elif 'message' in query or 'whatsapp' in query:
                try:
                    speak("To whom you want to send a message?")
                    phone_no = input("Please Enter the number of the Person You Want to send a Message:\n")
                    speak("What is the Message?")
                    message = takeCommandMic()
                    sendWhatsAppMsg(phone_no,message)
                    speak("Message has been Sent!")
                    
                except Exception as e:
                    print(e)
                    speak("Sorry, cannot send your message!")    

            elif 'wikipedia' in query:
                speak("Searching on Wikipedia...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query,sentences = 2)
                print(result)
                speak(result)

            elif 'search' in query or 'google' in query:
                searchGoogle()

            elif 'youtube' in query:
                playYT()

            elif 'weather' in query:
                weatherCall()

            elif 'news' in query:
                news()

            elif 'read' in query or 'clipboard'in query:
                textToSpeech()

            elif 'open' in query:
                if 'vs code' in query:
                    openVS()
                elif 'browser'in  query:
                    openEdge()
                elif 'documents'  in query:
                    os.system('explorer C://{}'.format(query.replace('Open',"")))

            elif 'joke' in query:
                sayJokes()

            elif 'screenshot' in query:
                screenshot()

            elif 'remember that' in query:
                rememberThings()

            elif 'do you know anything' in query:
                readRemembered()

            elif 'password' in query:
                passwordGenerator()

            elif 'flip' in query:
                flipCoin()

            elif 'roll' in query:
                rollDice()

            elif 'cpu' in query or 'usage' in query:
                cpuUsage()
                
            elif 'quit' in query or 'go now' in query or 'exit' in query or 'offline' in query:
                speak(f"{currentVoice} out!")
                flag = False