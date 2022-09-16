import datetime
import time
from playsound import playsound


def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm = "20:34"
 
        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M")
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm:
            print("Time to Wake up")
            # Playing sound
            playsound(u'alarm_sound.mp3')
            break

alarm()
