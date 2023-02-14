import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import pywhatkit
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your assistant. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e) 
        print("Say that again please...") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender@gmail.com', 'password')
    server.sendmail('sender@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'google classroom' in query:
            speak('opening google classroom')
            webbrowser.open("classroom.google.com")
        
        elif 'google meet' in query:
            speak('opening google meet')
            webbrowser.open("meet.google.com")
 
        elif 'gmail' in query:
            speak('opening google gmail')
            webbrowser.open("gmail.google.com")
 
        elif 'chrome' in query:
            speak('opening google chrome browser')
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("www.google.com")
 
        elif 'msbte' in query:
            speak('opening m s b t e official site')
            webbrowser.open("https://msbte.org.in/")
 
        elif 'whatsapp' in query:
            speak('opening whatsapp web')
            webbrowser.open("web.whatsapp.com")
        
        elif 'open stack overflow' in query:
            speak('opening stackoverflow')
            webbrowser.open("stackoverflow.com")

        elif 'open w3schools' in query:
            speak('opening w3schools')
            webbrowser.open("w3schools.com/python")
        
        elif 'open tutorials point' in query:
            speak('opening tutorialspoint')
            webbrowser.open("https://www.tutorialspoint.com/python")
        
        elif 'open geeksforgeeks' in query:
            speak('opening geeksforgeeks')
            webbrowser.open("geeksforgeeks.org/python")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")
        
        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receivers@gmail.com" 
                sendEmail(to, content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry my friend bhai. I am not able to send this email")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'play music from system' in query or 'play song from system' in query:
            music_dir = 'Music'
            songs = os.listdir(music_dir)
            print(songs) 
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'camera' in query:
            speak('opening camera')
            subprocess.run('start microsoft.windows.camera:', shell=True)
        
        elif 'paint' in query:
            speak('opening paint')
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint.lnk')

        elif 'calculator' in query:
            speak('opening calculator')
            os.startfile('C:\Windows\System32\calc.exe')
        
        
        elif 'edge' in query:
            speak('opening microsoft edge browser')
            os.startfile('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

       
        elif 'open file explorer' in query:
            speak('opening file explorer')
            os.startfile("explorer")
        
        elif 'notepad' in query:
            speak('opening notepad')
            os.system("Notepad")

        elif 'idle' in query:
            speak('opening python idle')
            os.startfile("C:\Program Files\Python310\Lib\idlelib\idle.pyw")
        
        elif 'word' in query:
            speak('opening microsoft word')
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
    
        elif 'powerpoint' in query:
            speak('opening microsoft powerpoint')
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")
        
        elif 'excel' in query:
            speak('opening microsoft excel')
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")

        elif 'access' in query:
            speak('opening microsoft access')
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Access.lnk")
        
        elif 'bye' in query:
            speak('Have a great day dear! meet you soon! bye!')
            exit()

        else:
            speak('I did not recognize')
            speak('say that again please!')










