# Python Code for sensors 
import RPi.GPIO as GPIO 
import time 
 
rled = 7 
oled = 5 
gled = 3 
buzzer = 10 
light = 16 
obstacle = 8 
gas = 12 
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(rled , GPIO.OUT) 
GPIO.setup(oled , GPIO.OUT) 
GPIO.setup(gled , GPIO.OUT) 
GPIO.setup(buzzer , GPIO.OUT) 
GPIO.setup(light, GPIO.IN) 
GPIO.setup(obstacle, GPIO.IN) 
GPIO.setup(gas, GPIO.IN) 
GPIO.output(buzzer,false) 
 
 
try: 
    while True: 
        lightsense = GPIO.input(light) 
        obstaclesense = GPIO.input(obstacle) 
        gassense = GPIO.input(gas) 
        if lightsense==False: 
            GPIO.output(rled,True) 
            GPIO.output(gled,True) 
            GPIO.output(oled,True) 
            print("Light sensed") 
        if lightsense==True: 
            GPIO.output(rled,False) 
            GPIO.output(gled,False) 
            GPIO.output(oled,False) 
            print("Light not sensed") 
        if obstaclesense==True: 
            GPIO.output(buzzer,True) 
            print("Obstacle sensed") 
            time.sleep(0.25) 
            GPIO.output(buzzer,False) 
            print("Obstacle sensed") 
            time.sleep(0.25) 
        if obstaclesense==False: 
            GPIO.output(buzzer,False) 
            print("Obstacle not sensed") 
        if gassense==True: 
            GPIO.output(buzzer,True) 
            print("Gass Sensed") 
            time.sleep(0.5); 
            GPIO.output(buzzer,False) 
            print("Gas Sensed") 
            time.sleep(0.5); 
        if gassense==False: 
            GPIO.output(buzzer,False) 
            print("Gass not sensed") 
    
except KeyboardInterrupt: 
    GPIO.cleanup() 
 
 
 
# Python Code for Testing Motors: 
import RPi.GPIO as GPIO 
import time  
 
 
# Define GPIO pins  
m11 = 16 
m12 = 18   
m21 = 38 
m22 = 40 
 
GPIO.setmode(GPIO.BCM)   
GPIO.setup(m11, GPIO.OUT) 
GPIO.setup(m12, GPIO.OUT) 
GPIO.setup(m21, GPIO.OUT) 
GPIO.setup(m22, GPIO.OUT) 
 
try: 
    while True: 
        GPIO.output(m11, GPIO.HIGH) 
        GPIO.output(m12, GPIO.LOW) 
        GPIO.output(m21, GPIO.HIGH) 
        GPIO.output(m22, GPIO.LOW) 
        time.sleep(5) 
 
        GPIO.output(m11, GPIO.LOW) 
        GPIO.output(m12, GPIO.HIGH) 
        GPIO.output(m21, GPIO.LOW) 
        GPIO.output(m22, GPIO.HIGH) 
        time.sleep(5) 
 
        GPIO.output(m11, GPIO.HIGH) 
        GPIO.output(m12, GPIO.LOW) 
        GPIO.output(m21, GPIO.LOW) 
        GPIO.output(m22, GPIO.HIGH) 
        time.sleep(5) 
 
        GPIO.output(m11, GPIO.LOW) 
        GPIO.output(m12, GPIO.HIGH) 
        GPIO.output(m21, GPIO.HIGH) 
        GPIO.output(m22, GPIO.LOW) 
        time.sleep(5) 
 
except KeyboardInterrupt: 
    GPIO.cleanup()