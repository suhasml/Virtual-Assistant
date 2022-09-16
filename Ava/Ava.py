import pyttsx3  #used to speak the text
import datetime
import speech_recognition as sr

#from alarm import alarm 
engine = pyttsx3.init("sapi5") #initializing the program
import random
import json
import torch
from brain import neuralnetwork
from neuron import bag_of_words,tokenize,stem
from basic_functions import time,date,joke,weather
from search import search
from website import open_website
from music import play_music

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json','r') as json_data:
    intents = json.load(json_data)

FILE = 'model.pth'
data = torch.load(FILE)
input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = neuralnetwork(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()


text = "Hello, I am Ava."
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',190)
    engine.say(text)   #speaks the text
    engine.runAndWait()  # wait until the speech is finished

    
def greeting():
    speak(text)
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning, How may I help you?")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon, How may I help you?")
    elif hour >= 18 and hour < 24:
        speak("Good evening, How may I help you?")
    else:
        speak("Good night, How may I help you?")


def TakeCommand():
    r = sr.Recognizer()   #initializing the speech recognition module
    with sr.Microphone() as source:     #using the microphone as source
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,3)   #listens to the user's voice, (0,2) -> recognizes the voice every 2 seconds
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #recognizes the user's voice
        #print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        #speak("Can you repeat again please...")
        return "None"
        
    return query



def Main(query):
    query = tokenize(query)
    x = bag_of_words(query,all_words)
    x = x.reshape(1,x.shape[0])
    x = torch.from_numpy(x)
    x = x.to(device)
    bye = [
                "thank you, looking forward to your next visit",
                "thank you, hope to see you again",
                "thank you, logging out",
                "thank you, goodbye"
            ]
    output = model(x)
    _, predicted = torch.max(output,1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output,dim=1)
    probs = probs[0][predicted.item()]

    if probs.item() > 0.5:
        for intent in intents['intents']:
            if intent['tag'] == tag:
                result = random.choice(intent['responses'])

                if 'time' in result:
                    time()
                    speak("Any other query?")
                    a=1
                
                elif 'date' in result:
                    date()
                    speak("Anything else that might interest you?")
                    a = 1

                elif 'joke' in result:
                    joke()
                    speak("Anything else that might interest you?")
                    a = 1
                
                elif 'search' in result:
                    search(query)
                    a = 1

                elif 'website' in result:
                    open_website(query)
                    a = 1

                elif 'weather' in result:
                    weather()
                    a = 1

                elif 'music' in result:
                    play_music()
                    a = 0
                
                #elif 'alarm' in result:
                #    alarm()
                    

                elif result in bye:
                    speak(result)
                    a=0

                else:
                    speak(result)
                    a = 1
                
                return a

