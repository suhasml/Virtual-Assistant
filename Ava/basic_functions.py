import datetime
import Ava
import pyjokes
from bs4 import BeautifulSoup
import requests

def time():
    time = datetime.datetime.now().strftime("%I:%M")   #gives the current time in 24 hour format
    Ava.speak("The current time is " + time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak_date =  "The current date is  " + str(day) + " " + str(month) + " " + str(year)
    Ava.speak(speak_date)


def joke():
    Ava.speak(pyjokes.get_joke())


def weather():
    Ava.speak("Which city do you want to know the weather of?")
    city = Ava.TakeCommand().lower()
    if city != 'none':
        res = requests.get("https://www.weather-forecast.com/locations/" + city + "/forecasts/latest")
        soup = BeautifulSoup(res.text, 'html.parser')
        info = soup.find_all('span', class_ = 'phrase')
        Ava.speak("The weather in " + city + " is " + info[0].text)
        Ava.speak("Anything else that might interest you? ")
    else:
        Ava.speak("Sorry, I could not understand. Can you ask again?")
        weather()
