import time

duration = float(input("How many minutes till you take a drink? "))

if duration < 1:
    print("Reminding you in", duration, "minutes")

elif duration > 1:
    print("Reminding you in", duration, "minutes")

else:
    print("Reminding you in", duration, "minute")

duration = duration * 60
# This converts duration from seconds to minutes

while 1 == 1:
    time.sleep(duration)
    print("Drink something")
# Find a way to stop this after a certain point