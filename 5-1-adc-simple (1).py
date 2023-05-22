import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def convert(chislo):
    ret = []
    while chislo != 0:
        ret.append(chislo % 2)
        chislo = chislo // 2
    for i in range(8 - len(ret)):
        ret.append(0)
    return ret[::-1]

def adc():
    for i in range(256):
        conv = convert(i)
        GPIO.output(dac, conv)
        value = GPIO.input(comp)
        time.sleep(0.05)
        if value == 0:
            return i
try:
    while True:
        number = adc()
        if number != 0:
            print(number, "{:.2f} Volts".format(3.3 * number / 256))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
