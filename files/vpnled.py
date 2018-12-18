#!/usr/bin/env python3
import psutil
from gpiozero import LED
from time import sleep

red = LED(17)

while True:
   if "vpnc" in (p.name() for p in psutil.process_iter()):
     red.off()
     sleep(0.25)
     red.on()
   else:
     red.off()
   sleep(10)