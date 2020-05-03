import time

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

while 1 == 1:
    time.sleep(duration)
    print("Drink something")