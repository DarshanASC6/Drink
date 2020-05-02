import time
duration = int(input("How many minutes till you take a drink? "))

duration = duration * 60
# This converts duration from seconds to minutes

print("Reminding you in", duration, "minutes")
time.sleep(duration)
print("Drink something")
# Try and run this in the terminal via a command