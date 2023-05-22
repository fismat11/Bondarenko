import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
for i in dac:
    GPIO.setup(i, GPIO.OUT)
    
def dec2bin(chislo):
    new = ""
    while chislo != 0:
        new = new + str(chislo % 2)
        chislo //= 2
    new = new + "0" * (8 - len(new))
    return new[::-1]

try:
    tim = int(input("Время периода: "))
    a = 0
    down = True
    while True:
        if a == 0:
            down = False
        elif a == 255:
            down = True
        for i in range(8):
            if dec2bin(a)[i] == "1":
                GPIO.output(dac[i], GPIO.HIGH)
            else:
                GPIO.output(dac[i], GPIO.LOW)
        time.sleep(tim / 255 / 2)
        if down:
            a = a - 1
        else:
            a = a + 1
finally:
    for i in dac:
        GPIO.output(i, GPIO.LOW)
    GPIO.cleanup()