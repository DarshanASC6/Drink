import time
duration = float(input("How many minutes till you take a drink? "))

duration = duration * 60
# This converts duration from seconds to minutes
print_duration = duration / 60

if print_duration == 1:
    print("Reminding you in", print_duration, "minute")
# if print_duration <= 
#     print("Reminding you in", print_duration, "minutes")

time.sleep(duration)
print("Drink something")
# Try and run this in the terminal via a command