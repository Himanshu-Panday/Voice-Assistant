import pyttsx3 #library for audio of assistant
import speech_recognition as sr #module which determine to assistant that it recognize what is being said
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') #api for assisstant's voice
voices = engine.getProperty('voices') #for getting the info. of voice property like it's male or female
# print(voices[1].id) #for printing the info. of voices
engine.setProperty('voice', voices[1].id) #for setting the voice property 0 for male and 1 for female


def speak(audio): #user defined func for speaking process
    engine.say(audio)
    engine.runAndWait()


def wishMe(): #user defined func to determine greetings to wish someone according to time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 16:
        speak("Good After Noon")

    else:
        speak("Good Evening")

    speak("I am Saturday developed by Himanshu A K A Harry, how may I help you") #executes after the greetings

def takeCommand(): #user defined func to take input and return defined output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #time gap taken by user is to be conisdered by this func
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said: {query}\n")        

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__": #here we write the function for whom we want response
    wishMe()
    while True:
        query = takeCommand().lower()  #determine that the query taken as input will always in small
        
        # logic for executing tasks

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open pc gamerz' in query:
            webbrowser.open("https://pcgamerzdrive.blogspot.com/")

        elif 'play music' in query:
            music_dir = 'E:\\Fav Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")