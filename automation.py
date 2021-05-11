from os import startfile
import pyautogui
from keyboard import press
from keyboard import write
from time import sleep
from keyboard import press_and_release
from time import sleep
import math
import pyttsx3 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[8].id) 
engine.setProperty('rate',180) 

def speak(audio) :
        print("  ")
        print(f" {audio} ")
        print("  ")
        engine.say(audio)
        engine.runAndWait() 


def whatsappmsg(name, message):
    startfile("E:\\WhatsAppSetup.exe")
    sleep(25)
    pyautogui.click(x=367, y=146)
    sleep(1)
    pyautogui.typewrite(name, interval=0.0)
    sleep(1)
    pyautogui.click(x=379, y=307)
    sleep(1)
    pyautogui.click(x=842, y=987)
    sleep(1)
    pyautogui.typewrite(message, interval=0.0)
    press('enter')


def whatsappcall(name):
    startfile("E:\\WhatsAppSetup.exe")
    sleep(30)
    pyautogui.click(x=367, y=146)
    sleep(1)
    pyautogui.typewrite(name, interval=0.0)
    sleep(1)
    pyautogui.click(x=379, y=307)
    sleep(1)
    pyautogui.click(x=1689, y=76)


def whatsappchat(name):
    startfile("E:\\WhatsAppSetup.exe")
    sleep(30)
    pyautogui.click(x=367, y=146)
    sleep(1)
    pyautogui.typewrite(name, interval=0.0)
    sleep(1)
    pyautogui.click(x=379, y=307)
    sleep(1)
    pyautogui.click(x=842, y=987)
    sleep(1)


def whatsappvideocall(name):
    startfile("E:\\WhatsAppSetup.exe")
    sleep(30)
    pyautogui.click(x=367, y=146)
    sleep(1)
    pyautogui.typewrite(name, interval=0.0)
    sleep(1)
    pyautogui.click(x=379, y=307)
    sleep(1)
    pyautogui.click(x=1638, y=70)


def chromeautomation(command):
    if "new tab" in command:
        speak("opening new tab")
        press_and_release("ctrl + t")

    elif "close tab" in command:
        speak("closing the tab")
        press_and_release("ctrl + w")

    elif "new window" in command:
        speak("opening the new window")
        press_and_release("ctrl + n")

    elif "history" in command:
        speak("opening the history")
        press_and_release("ctrl + h")

    elif "downloads" in command:
        speak("opening the downloads")
        press_and_release("ctrl + j")

    elif "bookmark" in command:
        speak("opening the bookmarks")
        press_and_release("ctrl + d")

    elif "incognito" in command:
        speak("opening incognito")
        press_and_release("ctrl + shift + n")

    elif "switch to tab" in command:
        command = command.replace("switch to tab", "")
        tab = int(command)
        speak(f"switching to tab {tab}") 
        press_and_release(f"ctrl + {tab}") 
        
    else:
        pass


def onbatterysavemode():
    speak("switching to battery saving mode")
    pyautogui.click(x=1881, y=1055)
    sleep(1)
    pyautogui.click(x=1631, y=616)
    sleep(1)
    pyautogui.click(x=1881, y=1055)


def onbluetooth():
    speak("switching on the bluetooth")
    pyautogui.click(x=1881, y=1055)
    sleep(1)
    pyautogui.click(x=1708, y=625)
    sleep(1)
    pyautogui.click(x=1881, y=1055)


def nightmode():
    speak("switching to night mode")
    pyautogui.click(x=1881, y=1055)
    sleep(1)
    pyautogui.click(x=1820, y=600)
    sleep(1)
    pyautogui.click(x=1881, y=1055)


def systemapps(command):
    command = command.replace("jarvis", "")
    command = command.replace("open", "")
    command = command.replace("service", "")
    speak(f"opening {command}")
    sleep(1)
    pyautogui.click(x=298, y=1064)
    pyautogui.typewrite(command, interval=0.0)
    sleep(2)
    pyautogui.click(x=417, y=387)


def youtubeautomate(command):
    command = command.replace("jarvis", "")
    command = command.replace("youtube", "")
    command = command.replace("video", "")
    if "pause" in command or "stop" in command:
        press("k")
    elif "resume" in command or "play" in command:
        press("k")
    elif "full screen" in command or "full screen mode" in command:
        press("f")
    elif "film screen" in command:
        press("t")
    elif "skip" in command:
        press("l")
    elif "back" in command:
        press("j")
    elif "increase play rate" in command or "speed up" in command or "increase" in command:
        press_and_release("shift + >")
    elif "decrease play rate" in command or "speed down" in command or "decrease" in command:
        press_and_release("shift + <")
    elif "previous video" in command or "previous" in command:
        press_and_release("shift + p")
    elif "next video" in command or "next" in command:
        press_and_release("shift + n")
    elif "mute" in command or "mute volume" in command:
        press("m")
    else:
        pass


def quickscan():
    pyautogui.click(x=298, y=1064)
    pyautogui.typewrite("quick scan", interval=0.0)
    sleep(1)
    pyautogui.click(x=417, y=387) 
    
    speak('sir , running a quick scan') 
    sleep(2) 
    pyautogui.click(x=694, y=481) 

def windowsupdate() :
    pyautogui.click(x=298, y=1064)
    pyautogui.typewrite("windows update", interval=0.0)
    sleep(1)
    pyautogui.click(x=417, y=387) 
    
    speak('sir , searching for updates') 
    sleep(2) 
    pyautogui.click(x=813, y=278) 

def commit() :
    speak("sir please write the message for commmit")
    message = input()   
    speak("commiting the changes to the master repository") 
    pyautogui.click(x=42, y=285)
    sleep(1)   
    pyautogui.click(x=186, y=148) 
    pyautogui.typewrite(message,interval=0.0)   
    pyautogui.click(x=257, y=86)  
    sleep(5) 
    speak("publishing changes to repository") 
    pyautogui.click(x=165, y=1011)
    sleep(1)
    pyautogui.click(x=42, y=285) 
    speak("sir you can proceed") 

def opennewfile() :
    speak("opening the new file") 
    press_and_release("ctrl + n") 


