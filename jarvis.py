
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
            from features import weather_forecast
            weather_forecast()

        elif "location" in query:
            from features import find_location
            find_location()

        elif "search in youtube" in query:
            speak("what do you wanna seach in youtube sir")
            search = take_command()
            from features import youtube_search
            youtube_search(search) 

        elif "play songs on youtube" in query:
            from features import play_song_yt
            play_song_yt()
            
        elif "set alarm" in query :
            from features import alarm
            alarm()     
        
        elif "search in google" in query or "open google" in query or "open chrome" in query :
            speak("what do you wanna search in google sir")
            search = take_command()
            from features import google_search
            google_search(search) 

        elif "go to sleep" in query or "sleep" in query :
            speak("ok sir, i am going to sleep you can call me at any time")
            break 

        elif "go offline" in query or "offline" in query :
            speak("ok sir i am going offlien") 
            speak("thank you sir for using me , have a nice day")
            sys.exit() 
         
        elif "what are my events" in query or "events" in query :
            import Quickstart 
            text = query
            service = Quickstart.authenticate_google()
            Quickstart.get_events(Quickstart.get_date(text),service)  
        
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
        from features import wish
        wish()
        # query = take_command()
        desire()
