#License: CC0
import RPi.GPIO as GPIO
import time

class SLX2016:
    def __init__(self,WR=4,A0=17,A1=18,D0=27,D1=22,D2=23,D3=24,D4=25,D5=5,D6=6,BL=12,CLR=13):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(0)
        GPIO.setup((WR,A0,A1,D0,D1,D2,D3,D4,D5,D6,BL,CLR),GPIO.OUT,initial=1)
        (self.WR,self.A0,self.A1,self.D0,self.D1,self.D2,self.D3,self.D4,self.D5,self.D6,self.BL,self.CLR) = (WR,A0,A1,D0,D1,D2,D3,D4,D5,D6,BL,CLR)
        self.APins = (A0,A1)
        self.DPins = (D0,D1,D2,D3,D4,D5,D6)

    def clear(self):
        GPIO.output(self.CLR,not 1)
        GPIO.output(self.CLR,not 0)

    def set_character(self,position,character):
        DSetting = ord(character)
        self.set_character_ascii(position,DSetting)

    def set_character_ascii(self,position,ascii):
        ASetting = '{0:02b}'.format(position)
        DSetting = '{0:07b}'.format(ascii)[::-1]
        for A in range(2):
            GPIO.output(int(self.APins[A]),int(ASetting[A]))
        GPIO.output(self.WR,not 1)
        for D in range(7):
            GPIO.output(int(self.DPins[D]),int(DSetting[D]))
        GPIO.output(self.WR,not 0)

    def set_string(self,string):
        self.clear()
        padded = string.rjust(4)
        for dig in range(4):
            self.set_character(3-dig,padded[dig])

    def blink(self,interval=0.1):
                GPIO.output(self.BL,not 1)
                time.sleep(interval)
                GPIO.output(self.BL,not 0)
                time.sleep(interval)
