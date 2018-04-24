# main.py -- put your code here!

from pyb import Pin 
from pyb import Timer

x1 = Pin('X1', Pin.OUT_PP)
x2 = Pin('X2', Pin.OUT_PP)

Do = 349
Re = 392
Mi = 440
Fa = 494
So = 523
La = 587
Si = 659

#Do = 2000    
#Re = 1500 
#Mi = 1000
#Fa = 500
#So = 400     
#La = 300 
#Si = 100

B11 = 200 
B21 = 250 

tone_end = -1
beat_end = -1

#tone_beat = [Do, B11, Re, B11, Mi, B11, Fa, B11, So, B11, La,B11, Si, B11, tone_end, beat_end]
tone_beat = [So, B21, Mi, B21, Mi, B21, Fa, B21, Re, B21, Re, B21,
             Do, B21, Re, B21, Mi, B21, Fa, B21, So, B21, So, B21, So, B21, 0, 0]

beat_value = 0 

def Buzzer(tone, beat):
    beat_value = beat
    while(beat_value > 0):
        x1.high()
        i = tone
        while(i):
            i = i - 1
        x1.low()
        i = tone
        while(i):
            i = i - 1
        beat_value = beat_value - 1

def PlayMusic():
    tone = 0
    beat = 1

    while(tone_beat[beat] > 0):
        tone = tone + 2
        beat = beat + 2
        Buzzer(tone_beat[tone], tone_beat[beat])

def f():
    beat_value = beat_value - 1

try:
    PlayMusic()
except:
    x1.low()

