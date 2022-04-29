import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
#print(voices[0].id)
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning!")
    elif hour>=12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")    
    speak("I am Terminator sir.Plz tell me how i can help you ")   

def takecommand():
    #It take microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing>>>>>>>")
        query=r.recognize_google(audio,language='en-np')
        print(f"user said:{query}\n")

    except Exception as e :
      #  print(e)

       print("Say it again PLz>>>>>>>>>>")
       return "None"
    return query 

def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",port=587)
    server.ehlo()
    server.starttls()
    server.login("prajjowl123@gmail.com",'Dahal@123')
    server.sendmail('prajjowl123@gmail.com',to,content)
    server.close()




if __name__=='__main__':
    wishme()
    #while(True):
    if 1:
      query=takecommand().lower()
    # Logic for Executing Task based on query 
    if 'wikipedia' in query:
        speak("Searching wikipedia")
        query=query.replace("wikipedia"," ")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube'in query:
        webbrowser.open("youtube.com")    
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open('stackoverflow.com')
    elif 'play music' in query:
        music_dir='C:\\Users\\Dell\\Documents\\music'
        songs=os.listdir(music_dir)  
        print(songs)  
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'stop music ' in query:
        music_dir='C:\\Users\\Dell\\Documents\\music'
        os.closefile()

    elif 'the time' in query:
        srtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir your time is  {srtime}")
        print(srtime)
    elif 'opencode' in query:
        path='C:\\Users\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\Programs\\Visual Studio Code' 
        os.startfile(path)   
    elif 'email to prashant' in query:
        try:
            speak("What should I say")
            to='dahalprashant10@gmail.com'
            content=takecommand()
            sendemail(to,content)
            speak("EMail has been sent ")
        except Exception as e:
            print(e)
            speak("Prajjowl ji I can sent the email Sry for Inconvinent")       
    
    elif 'stop' in query:
        print("stop")
        speak("ok sir i will not talk anymore ")
        speak("Sorry for inconvienence")
        exit()














    
    


    