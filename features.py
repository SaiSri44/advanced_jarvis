import datetime
import requests
import pyttsx3
from bs4 import BeautifulSoup 
import webbrowser
import os 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[8].id) 
engine.setProperty('rate',180) 
import pywhatkit as kit 

def speak(audio) :
        print("  ")
        print(f" {audio} ")
        print("  ")
        engine.say(audio)
        engine.runAndWait() 

def find_location(shout=True):
        try:
            r = requests.get("https://get.geojs.io/")
            ip_request = requests.get("https://get.geojs.io/v1/ip.json")
            ip_address = ip_request.json()['ip']

            url = "https://get.geojs.io/v1/ip/geo/" + ip_address + ".json"
            # # url to get the location
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()

            # # it will give data in the form of dictonary
            # # it mnay throw error sometimws because there may be no state for some plcaes like delhi
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            if shout:
                print(ip_address)
                print(geo_data)
                speech = f"Sir we are in {city} city in {state} region of  {country}"
                speak(speech)
            return city
        except:
            speak(
                "Sorry sir,due to poor internet i cannot find the location")
            # finding location takes more time ,so we added exception.
            pass

def weather_forecast(talk=True):
        place = find_location(shout=False)
        weather = "temperature in " + place
        url = f"https://www.google.com/search?q={weather}"
        r = requests.get(url)
        content = BeautifulSoup(r.text, "html.parser")
        temperature = content.find("div", class_="BNeawe").text
        if talk:
            speak(f"current {weather} is {temperature[:2]} degrees")
        else:
            return temperature       

def wish():
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
        temp = weather_forecast(talk=False) 
        if hour >= 0 and hour <= 12:
            speak(
                f"Good morning , it's {hour} : {minute}  a m , temperature outside is ,{temp[:2]} degrees")
        elif hour > 12 and hour <= 18:
            speak(
                f"Good Afternoon , it's {hour-12} : {minute} p m , temperature outside is ,{temp[:2]} degrees")
        else:
            speak(
                f"Good Evening , it's {hour-12} : {minute} p m , temperature outside is ,{temp[:2]} degrees")
        speak("Hii Sir, I am jarvis, please tell how can i help you") 

def youtube_search(search) :
    url =  "https://www.youtube.com/results?search_query="  +search
    speak("searching in the youtube")
    webbrowser.open(url) 
    speak("sir , this is what i found on youtube")

def play_song_yt() :
    speak("playing songs on youtube")
    kit.playonyt("jala jala patham nuvu") 

def alarm() :
    Time = open("C:\\Users\\angaj\\OneDrive\\Desktop\\jarvis2\\features of jarvis\\data.txt",'a') 
    speak("sir, please enter the time for alarm") 
    alaram_time = input() 
    Time.write(alaram_time) 
    Time.close() 
    os.startfile("C:\\Users\\angaj\\OneDrive\\Desktop\\jarvis2\\database\\extraprogramm\\Alarm.py")  

def google_search(search) :
    if search == None :
        speak("sir , you did not mention anything to search ,so i am stopped searching ") 
    else :    
        search = search.replace("search for","")
        search = search.replace("jarvis","")
        speak(f"searching for {search} in google") 
        webbrowser.open(search)
        speak("sir , this is what i found in the google") 

        
