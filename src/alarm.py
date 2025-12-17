"""
Alarm Module

Implements time-based alarm and reminder functionality
for the Python personal assistant.
"""

import winsound
import datefinder
import datetime
import playsound


def alarm(text):
    dTimeA = datefinder.find_dates(text)
    for mat in dTimeA:
        print(mat)
    stringA = str(mat)
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA)
    minA = timeA[3:-3]
    minA = int(minA)


    while True:
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                print('alarm')
                winsound.PlaySound('',winsound.SND_LOOP)#location of the audio
            elif minA<datetime.datetime.now().minute:
                break
#alarm('set an alarm at 4:52 pm')
