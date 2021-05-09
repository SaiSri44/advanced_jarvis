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

def wolfram(query) :
    import wolframalpha
    api_key = "YQRJPU-PULT2Y3QX3"
    requester = wolframalpha.Client(api_key) #requesting the information from the wolframalpha database
    if "outside" in query or "surroundings" in query:
        location  = find_location(shout=False)
        query = query.replace("outside",location) 
        
    else :
       
        requested  = requester.query(query)    

    try :
       requested = requester.query(query) #asking for the answer for our query
       Answer = next(requested.results).text #answer might be text or videos or pictures,but we want only text so extracting only text from the answer provided by the wolframalpha, the answer may not find in the database so we included it in the try block 
       return Answer 
    except:
        speak("sir, your query is not processed ,sorry for the inconvenience") 
        return "error" 

def calculator(query) :
    query = query.replace("jarvis","")
    query = query.replace("calculate","")
    query = query.replace("into","*")
    query = query.replace("minus","-")
    query = query.replace("plus","+")
    query = query.replace("divided by","/") 
    query = query.replace("multiply","*") 
    query = query.replace("power","^") 
    print(f"{query} = " ,end=" ") 
    result = wolfram(query) 
    if result!="error" :
      print(f"{result}") 
      speak(f"the result of the calculation is {result}") 

def input_calculator(query) :
    print(f"{query} = ", end=" ") 
    result = wolfram(query)
    if result!= "error" :
       print(f"{result}")
       speak(f"the result of the calculation is {result}") 

def taking_screen_shot():
        speak("sir,please tell me the name of this screenshot file")
        name = take_command().lower()
        speak("Hang on for few seconds sir , I am taking the screenshot")
        time.sleep(3)
        img = pyautogui.screenshot() 
        img.save(f"{name}.jpg")
        speak(
            "ok sir i am done with taking screenshot, it is saved in our current folder, i am ready for another command sir")
    
 
# print(wolfram("days until may 24 2021"))  
  
# print(calculate("2 into 3 plus 4 power 2"))         