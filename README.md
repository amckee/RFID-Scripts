# RFID-Scripts
Various scripts written for RFID stuff

This script, for a Raspberry Pi, will read card data from a scanner wired into the serial I/O ports (TXD0 and RXD0) and when the hardcoded card ID is confirmed then it toggles pin 23 on/off.

For some fun testing I've used this pin to control a relay, but it of course could be anything.
