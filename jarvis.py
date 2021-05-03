from features import *
import pyttsx3
import speech_recognition as sr
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[8].id)
engine.setProperty('rate', 180)


def speak(audio):
    print("  ")
    print(f" {audio} ")
    print("  ")
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
        except:
            pass
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except sr.RequestError:
        print(
            "Could not request the results from the google speech recognition service.... ")
        return "poor connection"
    except:
        return None
    return query.lower()


def desire():
    while True:
        query = take_command()
        if query == None:
            pass

        elif "temperature" in query:
            weather_forecast()

        elif "location" in query:
            find_location()

        elif "search in youtube" in query:
            speak("what do you wanna seach in youtube sir")
            search = take_command()
            youtube_search(search) 

        elif "play songs on youtube" in query:
            play_song_yt()
            
        elif "set alarm" in query :
            alarm()     
       

while True:
    query = take_command()
    if "poor connection" == query:
        speak(
            "Sir,due to poor internet connection , i am not able to follow your commands, please connect to internet sir")
        speak(
            "sir,i will wait for 10 seconds, for you to connect to internet ")
        time.sleep(10)
        speak("ok sir i am done,i hope your are connected to internet")
        query = take_command()
        if "poor connection" == query:
            speak(
                "sir, i think you don't have proper intenet connection, so i am going offline")
            sys.exit()
    elif None == query:
        pass
    elif "hello jarvis" in query:
        wish()
        # query = take_command()
        desire()
