import datetime as d
from datetime import datetime
import wikipedia
import pyttsx3 
import speech_recognition as sr
import keyboard as k
import webbrowser as wb
import colorama
from colorama import Fore
import pyfiglet
from pyfiglet import Figlet
import playsound
from playsound import playsound
colorama.init()
import time

x= pyttsx3.init('sapi5')
x.setProperty('rate', 155)
voices = x.getProperty('voices')
x.setProperty('voice', voices[0].id)




def render(text, style):
    f = Figlet(font=style)
    print('\n'*5)
    print(f.renderText(text))

render('Friday', 'banner3-D')


def speak(audio):
    x.say(audio)
    x.runAndWait()

def wishMe():
    hour = int(d.datetime.now().hour)
    if hour>= 6 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    elif hour>=19 and hour<0:
        speak("Good night Sir !") 
    else:
        speak('Sir, you should go to bed')
  
    
    
    


    
    
    
    


def command():
    r= sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=1)
        playsound("C:\\Users\\Adam\\Music\\music\\noti.wav")
        print(Fore.LIGHTRED_EX+'\nListening\n')
        audio = r.listen(mic, phrase_time_limit=5)
    try:
        query = r.recognize_google(audio,language='en-US')
        print(Fore.LIGHTMAGENTA_EX+f'You said: {Fore.CYAN+query}')
    except sr.UnknownValueError:
        print(Fore.YELLOW+'\nFailed to hear you sir\n')
        return "None"
    
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        
        if k.is_pressed('down'):
            query = command().lower()
            if 'youtube' in query:
                wb.open_new('https://www.youtube.com')
                playsound("C:\\Users\\Adam\\Music\\music\\noti.wav")

                speak('Opening youtube')
            elif 'info' in query:
                speak('What do you want to know sir?')
                
                inform = command().title()
                inform.title()
                list = wikipedia.search(inform)
                playsound("C:\\Users\\Adam\\Music\\music\\noti.wav")

                inform = list[0]
                print(f"\n{inform}\n")
                b = wikipedia.summary(inform, auto_suggest=0)
                print(Fore.LIGHTGREEN_EX+b)
                speak(f'Searching information about {inform}. Sir, why are you so stupid? {inform} is a,{b}')
            elif 'math' in query:
                speak('Bruh sir you failed math? What you want from me?')
                quest = command().lower()
                wb.open_new('https://www.google.com/search?q='+quest) 
                playsound("C:\\Users\\Adam\\Music\\music\\noti.wav")

            elif 'none' in query:
                speak('Sorry')
            else:
                speak('Sorry sir, but i cant understand your command. wanna search it on google or youtube?')
                q = command().lower()
                if 'youtube' in q:
                    wb.open_new('https://www.youtube.com/results?search_query='+query)
                    playsound("C:\\Users\\Adam\\Music\\music\\noti.wav")

                    speak(f'Searching {query} on youtube')
                elif 'google' in q:
                    wb.open_new('https://www.google.com/search?q='+query)
                    time.sleep(1)
                    playsound("C:\\Users\\Adam\\Music\\music\\noti.wav")
                    
                    speak(f'Searching {query} on google')
                elif 'never mind' in q:
                    speak('Okay sir')
            
            
                
            
                
        
                

