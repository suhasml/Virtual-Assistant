import imp
import Ava
import webbrowser as wb
import time


browser = "C:/Users/suhas/AppData/Local/Programs/Opera GX/opera.exe %s"

def youtube():
    Ava.speak("What video would you like to see?")
    ip = Ava.TakeCommand().lower()
    if ip != 'none':
        wb.get(browser).open("https://www.youtube.com/results?search_query="+ip)
        Ava.speak("Here is what I found for you.")
        Ava.speak("Anything else that might interest you? ")
    else:
        Ava.speak("Sorry, I could not understand. Can you ask again?")
        youtube()
    return

def open_website(query):

    if 'youtube' in query:
        youtube()
        return

    elif query != 'none':
        Ava.speak("What would you like to search for?")
        ip = Ava.TakeCommand().lower()
        if 'youtube' in ip:
            youtube()
            return
        else:
            url = "https://www.google.com.tr/search?q={}".format(ip)
            wb.get(browser).open(url)
            Ava.speak("Here is what I found for you.")
            time.sleep(1)
            Ava.speak("Anything else that might interest you? ")
            
    else:
        Ava.speak("Sorry, I didn't understand that.")
        Ava.speak("Anything else that might interest you? ")    
        open_website()               
    #wb.register('opera', None,wb.BackgroundBrowser(browser),1)
    return 