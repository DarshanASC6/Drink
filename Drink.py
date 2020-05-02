import time
duration = float(input("How many minutes till you take a drink? "))
# This converts duration from seconds to minutes

if duration < 1:
    print("Reminding you in", duration, "minute")

elif duration > 1:
    print("Reminding you in", duration, "minute")

else:
    print("Reminding you in", duration, "minutes")

duration = duration * 60

time.sleep(duration)

print("Drink something")
# Try and run this in the terminal via a command