from os import startfile
import pyautogui
from keyboard import press
# from keyboard import write
from time import sleep


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
