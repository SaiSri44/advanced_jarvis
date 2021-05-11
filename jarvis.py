import webbrowser
import os
from features import wish
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
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
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
            from features import wolfram
            query = query.replace("jarvis", "")
            query = query.replace("what is", "")
            speak("sir , please be patient , fetching temperature might take time")
            if wolfram(query) != "error":
                speak(f" {query} is {wolfram(query)} ")

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

        elif "set alarm" in query:
            from features import alarm
            alarm()

        elif "search in google" in query or "open google" in query or "open chrome" in query:
            speak("what do you wanna search in google sir")
            search = take_command()
            from features import google_search
            google_search(search)

        elif "go to sleep" in query or "sleep" in query:
            speak("ok sir, i am going to sleep you can call me at any time")
            break

        elif "go offline" in query or "offline" in query:
            speak("ok sir i am going offlien")
            speak("thank you sir for using me , have a nice day")
            sys.exit()

        elif "what are my events" in query or "events" in query:
            import Quickstart
            text = query
            service = Quickstart.authenticate_google()
            Quickstart.get_events(Quickstart.get_date(text), service)

        elif "power" in query or "-" in query or "into" in query or "+" in query or "multiply" in query or "divided by" in query:
            from features import calculator
            speak("hang on sir, i am calculating")
            calculator(query)

        elif "calculate" in query or "find" in query or "calculation" in query:
            speak("sir,please enter the calculation")
            calci = input()
            from features import input_calculator
            input_calculator(calci)

        elif "screenshot" in query:
            from features import taking_screen_shot
            taking_screen_shot() 

        elif "send whatsapp message" in query or "message" in query :
            from automation import whatsappmsg
            speak("sir ,whom do you want to send the message ")
            name = take_command()
            while name == None :
                speak("sir, i could n't recognize please tell again") 
                name = take_command() 
            speak("sir, tell me what's the message ")
            message = take_command()
            speak(f"sending whatsapp message to {name} ") 
            whatsappmsg(name,message) 

        elif "voice call" in query or "whatsapp call" in query  :
            from automation import whatsappcall
            speak("sir , whom do you wanna call")    
            name = take_command()
            while name == None :
                speak("sir, i did not recognize it please tell agian") 
                name = take_command()
            speak(f"calling the {name}") 
            whatsappcall(name) 

        elif "video call"  in query or "whatsapp video call" in query : 
            from automation import whatsappvideocall
            speak("sir ,  whom do you wanna make a video call")     
            name = take_command()
            while name ==  None :
                speak("sir, i did not recognize it , please tell again") 
                name = take_command()
            speak(f"making the videocall to {name}")    
            whatsappvideocall(name) 
        
        elif "whatsapp chat" in query or "chat" in query :
            from automation import whatsappchat
            speak("sir , whose chat do you wish to open")
            name = take_command()
            while name == None :
                speak("sir , i did not recognize it , please tell again")
                name = take_command()
            speak(f"opening the whatsapp chat of {name}")    
            whatsappchat(name) 
         
        elif "open instagram" in query or "instagram" in query :
            speak("opening instagram") 
            webbrowser.open("https://www.instagram.com/")

        elif "open facebook" in query or "facebook"  in query :
            speak("opening facebook")     
            webbrowser.open("https://www.facebook.com/")

        elif "open linkedin" in query or "linkedin" in query :
            speak("opening linkedin")    
            webbrowser.open("https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin") 

        elif "open github" in query or "github" in query :
            speak("opening the github")    
            webbrowser.open("https://github.com/") 
       
        elif "open notepad" in query  :
            speak("opening notepad")
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(path) 

        elif "open command prompt" in query :
            speak("opening command prompt")    
            os.system("start cmd")
       
        elif "close notepad" in query or "stop notepad" in query or "exit notepad" in query :
            speak("closing notepad") 
            os.system("TASKKILL /f /im notepad.exe") 

        elif "close command prompt" in query or "stop command prompt" in query or "exit command prompt" in query :
             speak("closing command prompt")
             os.system("TASKKILL /f /im cmd.exe")

        elif "close google" in query or "close chrome" in query :
             os.system("TASKKILL /f /im chrome.exe")    

        elif "open whatsapp" in query :
            speak("opening whatsapp")
            path = "C:\\Users\\angaj\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(path)     

        elif "close whatsapp"  in query or "stop whatsapp" in query or "exit whatsapp" in query :
            speak("closing whatsapp") 
            os.system("TASKKILL /f /im WhatsApp.exe")    

        elif "open youtube" in query :
           speak("opening youtube")
           webbrowser.open("https://www.youtube.com/")

        elif "new tab" in query or "history" in query or "downloads" in query or "close tab" in query or "new window" in query or "bookmark" in query or "switch to tab" in query or "incognito" in query : 
            from automation import chromeautomation
            chromeautomation(query)   

        elif "bluetooth" in query :
            from automation import onbluetooth
            onbluetooth()

        elif "night mode" in query or "night" in query :
            from automation import nightmode
            nightmode()

        elif "battery saver" in query or "saver" in query :
            from automation import onbatterysavemode
            onbatterysavemode()         

        elif "open" in query :
            from automation import systemapps
            systemapps(query)  

        elif  "youtube" in query or "skip" in query or "back" in query or "next" in query or "previous" in query or "video" in query or "mute" in query or "full screen" in query or "play" in query or "resume" in query or "stop" in query :
            from automation import youtubeautomate
            youtubeautomate(query)  
       
        elif "quick scan" in query or "scan" in query :
           from automation import quickscan
           quickscan() 
       
        elif "windows update" in query or "updates" in query :
           from automation import windowsupdate
           windowsupdate()  
#      
# while True: 
#     query = take_command() 
#     if "poor connection" == query:
#         speak(
#             "Sir,due to poor internet connection , i am not able to follow your commands, please connect to internet sir")
#         speak(
#             "sir,i will wait for 10 seconds, for you to connect to internet ")
#         time.sleep(10)
#         speak("ok sir i am done,i hope your are connected to internet")
#         query = take_command()
#         if "poor connection" == query:
#             speak(
#                 "sir, i think you don't have proper intenet connection, so i am going offline")
#             sys.exit()
#     elif None == query:
#         pass
#     elif "hello jarvis" in query:
#         from features import wish 
#         wish()
#         # query = take_command()
#         desire() 


wish() 
desire() 
