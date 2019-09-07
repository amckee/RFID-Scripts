#!/usr/bin/python3
# scan card info, then store in log file

from gpiozero import LED
from time import sleep
import serial
import datetime

cardlog = "/home/pi/rfid_cards.log"
# debugging card number
cardNumber = "0200583CF395" #very hackish, I know, but this is just a prototype
serialdev = "/dev/ttyAMA0"
led = LED(21)
relay = LED(23)

led.off()
relay.off()
ser = serial.Serial( serialdev, baudrate=9600, bytesize=8 )
log = open( cardlog, 'a' )

def main_loop():
    cardID = ""
    print("Waiting for card...")
    while True:
        rdat = ser.read()
        if rdat == b'\x02': # start of data
            pass
        elif rdat == b'\x03': # end of data
            tstamp = datetime.date.strftime( datetime.datetime.today(), '%Y.%m.%d %H:%M:%S' )
            print( cardID )
            log.write( "[%s] %s\n" % (tstamp, cardID) )
            log.flush()
            if cardID == cardNumber:
                print("Valid card detected.")
                led.toggle()
                relay.toggle()
            else:
                print("Invalid card detected.")
            cardID = ""
        else: # actual card data; append to variable
            cardID = cardID + rdat.decode("utf-8")
    print("Main loop exited")


main_loop()

log.close()
ser.close()
