# BrightnessToggler
# Author: Sandro Zappulla
# Github: @SandroZappulla
# version: v1.0

# Installation:
# python -m pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org screen-brightness-control
# IMPORT
import screen_brightness_control as sbc

# list of all monitor names
all_monitors = sbc.list_monitors()
# count all monitor names (to get maximum amount of connected monitors)
count_monitors = len(all_monitors)
# output of all monitor brightness level in an array 
all_brightness = sbc.get_brightness()

# variable - counter & value array
value = []
counter = 0

# condition: to get an value array (verify that all monitors have brightness of 100%)
while counter < count_monitors:
    counter= counter + 1
    value.append(100)
#print(value)

print(count_monitors)

# Condition: then all monitors got the brightness level of 100%
# All monitors toggle the brightness to the toggle_value
toggle_value = 50

if all_brightness == value:
    sbc.set_brightness(toggle_value)
else:
    sbc.set_brightness(100)


# if you like to use any specific monitor for brightness level then use this upcoming lines
#sbc.set_brightness(100, display=0)
#sbc.set_brightness(100, display=1)
#sbc.set_brightness(100, display=2)