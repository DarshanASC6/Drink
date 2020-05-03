import time
import ctypes  # An included library with Python install.   

duration = float(input("How many minutes till you take a drink? "))
# Asks the user how frequently they want to be reminded to take a drink

if duration < 1:
    print("Reminding you in", duration, "minutes")
# Basic grammer stuff because I'm picky

elif duration > 1:
    print("Reminding you in", duration, "minutes")
# Basic grammer stuff because I'm picky

else:
    print("Reminding you in", duration, "minute")
# Basic grammer stuff because I'm picky


duration = duration * 60
# This converts duration from seconds to minutes

counter = 0
# Variable that counts the number of reminders printed

while 1 == 1:
    time.sleep(duration)
    # Waits for the user input amount of time
    
    ctypes.windll.user32.MessageBoxW(0, "Drink something", "Drink.py Reminder", 0)
    # Creates a popup message that won't go away until the user acknowledges it
    
    counter = counter + 1
    # Increases the number of reminders

    print("Reminders given: ", counter)