from os import startfile
import pyautogui
from keyboard import press
from keyboard import write
from time import sleep
from keyboard import press_and_release
from time import sleep
import math
from features import speak

def whatsappmsg(name, message):
    startfile("E:\\WhatsAppSetup.exe")
    sleep(25)
    pyautogui.click(x=367, y=146)
    sleep(1)
    pyautogui.typewrite(name, interval=0.3)
    sleep(1)
    pyautogui.click(x=379, y=307)
    sleep(1)
    pyautogui.click(x=842, y=987)
    sleep(1)
    pyautogui.typewrite(message, interval=0.3)
    press('enter')


def whatsappcall(name):
    startfile("E:\\WhatsAppSetup.exe")
    sleep(30)
    pyautogui.click(x=367, y=146)
    sleep(1)
    pyautogui.typewrite(name, interval=0.3)
    sleep(1)
    pyautogui.click(x=379, y=307)
    sleep(1)
    pyautogui.click(x=1689, y=76)


def whatsappchat(name):
    startfile("E:\\WhatsAppSetup.exe")
    sleep(30)
    pyautogui.click(x=367, y=146)
    sleep(1)
    pyautogui.typewrite(name, interval=0.3)
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
    pyautogui.typewrite(name, interval=0.3)
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

    elif "new window" in command :
        speak("opening the new window")
        press_and_release("ctrl + n")

    elif "history" in command :
        speak("opening the history")
        press_and_release("ctrl + h") 

    elif "downloads" in command :
        speak("opening the downloads")
        press_and_release("ctrl + j") 

    elif "bookmark" in command :
        speak("opening the bookmarks")
        press_and_release("ctrl + d")

    elif "incognito" in command :
        speak("opening incognito")
        press_and_release("ctrl + shift + n")

    elif "switch tab" in command :
        speak("switching to new tab") 
        command = command.replace("switch tab to", "")
        tab = int(command)
        press_and_release(f"ctrl + {tab}") 
    else :
        pass


