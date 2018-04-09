import urllib2, urllib
import time
import sys
import datetime
import re
import wiringpi
import Adafruit_CharLCD as LCD


lock = #lockname
door = #doorname

currentlock = '3'
currentdoor = '2'

wiringpi.wiringPiSetup()

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


#Pin Definitions

LOCKPIN1 = 24
LOCKPIN2 = 25
MOTORF = 22
MOTORB = 23

#Function Definitions

def doorOpen():		
    wiringpi.pinMode(LOCKPIN1,1)
    wiringpi.pinMode(LOCKPIN2,1)
    wiringpi.pinMode(MOTORF,1)
    wiringpi.pinMode(MOTORB,1)
    print "Door Unlocked"
    wiringpi.digitalWrite(LOCKPIN1,1)
    wiringpi.digitalWrite(LOCKPIN2,0)
    print "ALERT! DOOR MOVING!"
    wiringpi.digitalWrite(MOTORF,1)
    wiringpi.digitalWrite(MOTORB,0)
    time.sleep(3)
    wiringpi.digitalWrite(LOCKPIN1,0)
    wiringpi.digitalWrite(LOCKPIN2,0)
    wiringpi.digitalWrite(MOTORF,0)
    wiringpi.digitalWrite(MOTORB,0)
    print "DOOR STOPPED!"

def doorClose():
    wiringpi.digitalWrite(MOTORF,0)
    wiringpi.digitalWrite(MOTORB,1)
    print "ALERT! DOOR MOVING!"
    time.sleep(3)
    wiringpi.digitalWrite(MOTORF,0)
    wiringpi.digitalWrite(MOTORB,0)
    print "DOOR STOPPED!"

def lcdDisplay(arg1, arg2):
    
    lcd.message(arg1+'\n'+arg2)
    time.sleep(2)

#main
while True: 
    # 'Checking lock status'
    path='http://munro.humber.ca/~n01137746/display.php?pname='+lock
    
    req=urllib2.Request(path)
    req.add_header("Content-type", "application/x-www-form-urlencoded")

    page=urllib2.urlopen(req).read()

    databaseval = re.sub("<.*?>", "", page)
    databaseval = databaseval.replace('\n','')
    databaseval = databaseval.replace(":       ",":\n")
    databaseval = databaseval.strip(' ')

    lockval = ''

    if databaseval == '3' and databaseval == currentlock:
        lockval = 'Lock is armed'
    elif databaseval=='3' and databaseval != currentlock:
        lockval = 'Lock has been armed by the application'
        currentlock = databaseval
    elif databaseval=='4' and databaseval==currentlock:
        lockval = 'Lock is disarmed'
    elif databaseval=='4' and databaseval != currentlock:
        lockval = 'Lock has been disarmed by the application'
        currentlock = databaseval

    # Checking door status    
    path='http://munro.humber.ca/~n01137746/display.php?pname='+door
    
    req=urllib2.Request(path)
    req.add_header("Content-type", "application/x-www-form-urlencoded")

    page=urllib2.urlopen(req).read()

    databaseval = re.sub("<.*?>", "", page)
    databaseval = databaseval.replace('\n','')
    databaseval = databaseval.replace(":       ",":\n")
    databaseval = databaseval.strip(' ')

    doorval = ''
           
    if databaseval == '1' and currentdoor == '2':
        doorval = 'Door is closed'
        lcdDisplay(doorval,lockval)
    elif databaseval == '1' and currentdoor == '0':
        doorval = 'Door is open'
        lcdDisplay(doorval,lockval)
    elif databaseval == '2':
        doorval = 'Door is opening'
        currentdoor = '0'
        lcdDisplay(doorval,lockval)
        doorOpen()
    elif databaseval == '0':
        doorval = 'Door is closing'
        currentdoor = '2'
        lcdDisplay(doorval,lockval)
        doorClose()
        
    time.sleep(1)
    
    lcd.clear()
