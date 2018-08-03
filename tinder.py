from pynput.keyboard import Key, Controller
import random, time, requests
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

keyboard = Controller()

def swipeLeft():
    keyboard.press(Key.left)#press left
    time.sleep(0.6)
    keyboard.release(Key.left)  
    return

def swipeRight():
    keyboard.press(Key.right)#press right
    time.sleep(0.6)
    keyboard.release(Key.right)
    for n in range (0,5):
        keyboard.press(Key.esc)#press escape
        time.sleep(0.3)
        keyboard.release(Key.esc)
    return

def tab():
    #tab presses
    keyboard.press(Key.tab)#press once
    time.sleep(1)
    keyboard.release(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab)#press second time
    time.sleep(1)
    keyboard.release(Key.tab)
    time.sleep(1)


def main():

    #age pref is integer taken by user, should be in the range of their profile or it wont work
    agePref = input("Enter age preference in range of your profile.\nIf no preference, enter nothing: ")
    schoolPref = input("Swipe right on usc/ucla students?\nIf not, enter nothing: ")
    if not agePref and not schoolPref:#no age pref, so ask user to swipe left or right and how many times
        leftOrRight = input("Do you want to swipe left or right?: ")
    times = input("How many times do you want to swipe left or right?: ")
    
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\Karalee\\AppData\\Local\Google\\Chrome\\User Data\\Default")
    driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe",chrome_options=options)
    driver.get('https://tinder.com/')
    time.sleep(3)
    tab()
    school = driver.find_elements(By.XPATH, '//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[4]/div[1]/span')
    age = driver.find_elements(By.XPATH, '//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[5]/div[1]/div/span[2]')
    if agePref:
        print ("age entered succesfully")
        agePref = ", " + agePref#convert age pref to ", ##" format
        for n in range (0, int(times)):
            age = driver.find_elements(By.XPATH, '//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[5]/div[1]/div/span[2]')
            if age:#age found
                ageNum = age[0].text
                if agePref == ageNum:
                    swipeRight()
                else:
                    swipeLeft()
            else:#age not found
                swipeLeft()
    elif schoolPref:#swipe right on ucla/usc students
        print("okay, will swipe right on all usc/ucla students")
        for n in range (0,int(times)):
            school = driver.find_elements(By.XPATH, '//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[4]/div[1]/span')
            if school: #profile has school name in it
                schoolName = school[0].text.lower()
                if(schoolName=="usc" or schoolName=="university of southern california" or\
                   schoolName=="university of so cal" or schoolName=="ucla" or\
                   schoolName=="university of california los angeles" or schoolName=='uc los angeles'\
                   or schoolName=="university of california la" or schoolName=="university of california, la"\
                   or schoolName=="university of california, los angeles"):
                    swipeRight()
                else:
                    swipeLeft()#school name doesnt match usc or ucla
            else:
                swipeLeft()
                

    else:#no age pref, so swipe left or right n amount of times
        if leftOrRight == "right" or leftOrRight == "RIGHT":
            for n in range (0, int(times)):
                swipeRight() 
        elif leftOrRight == "left" or leftOrRight == "LEFT":
            for n in range (0, int(times)):
                swipeLeft()

if __name__ == "__main__":
    main()






