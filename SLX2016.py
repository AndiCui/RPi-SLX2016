#    CC0




import RPi.GPIO as GPIO
import time

class SLX2016:
    def __init__(self,WR,A0,A1,D0,D1,D2,D3,D4,D5,D6,CLR):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup((WR,A0,A1,D0,D1,D2,D3,D4,D5,D6,CLR), GPIO.OUT, initial=1)
        (self.WR,self.A0,self.A1,self.D0,self.D1,self.D2,self.D3,self.D4,self.D5,self.D6,self.CLR) = (WR,A0,A1,D0,D1,D2,D3,D4,D5,D6,CLR)
        self.Apins = (A0,A1)
        self.Dpins = (D0,D1,D2,D3,D4,D5,D6)
    
    def clr(self):
        GPIO.output(self.CLR,not 1)
        GPIO.output(self.CLR,not 0)
    
    def char(self, pos, char):
        Asetting = '{0:02b}'.format(pos)
        Dsetting = '{0:07b}'.format(ord(char))[::-1]
        for A in range(2):
            GPIO.output(int(self.Apins[A]),int(Asetting[A]))
        time.sleep(0.250)
        GPIO.output(self.WR,not 1)
        for D in range(7):
            GPIO.output(int(self.Dpins[D]),int(Dsetting[D]))
        GPIO.output(self.WR,not 0)
        time.sleep(0.250)
    
    def bin(self, pos, Dsetting):
        Asetting = '{0:02b}'.format(pos)
        for A in range(2):
            GPIO.output(int(self.Apins[A]),int(Asetting[A]))
        time.sleep(0.250)
        GPIO.output(self.WR,not 1)
        for D in range(7):
            GPIO.output(int(self.Dpins[D]),int(Dsetting[D]))
        GPIO.output(self.WR,not 0)
        time.sleep(0.250)

    def str(self, str):
        self.clr()
        padded = str.rjust(4)
        for dig in range(4):
            self.char(3-dig, padded[dig])


