# BrightnessSetter
# Author: Sandro Zappulla
# Github: @SandroZappulla
# version: v1.0

import screen_brightness_control as sbc
import os

print("Monitor Helligkeit Setter v1.0 by Sandro Zappulla")
helligkeit_eingabe = int(input("Bitte Helligkeit aller Monitore eingeben: \n"))


sbc.set_brightness(helligkeit_eingabe, display=0)
sbc.set_brightness(helligkeit_eingabe, display=1)
sbc.set_brightness(helligkeit_eingabe, display=2)