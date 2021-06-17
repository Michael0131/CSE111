print("")
from datetime import datetime
current_time = datetime.now()
weekday = current_time.isoweekday()
datatime = datetime
week_day = 0
import time
datetime_element = datetime(2020, 7, 10, 12, 56, 54, 324893)
date_element = datetime_element.date()
time_current = time.strftime("%H:%M:%S") 
time_current = time.strftime("%H:%M:%S")
#tire Shop Code
#Welcome user
print("")

#import math
import math

print("Welcome to Mike's Tire Shop! To find the volume of your tire,")
print("")
# Set days
if weekday ==1:
    print(f"Today is Monday")
    print(f"the date is: {str(date_element)}")
    print(f"The time is: {time_current}")
if weekday ==2:
    print(f"Today is Tuesday")
    print(f"the date is: {str(date_element)}")
    print(f"The time is: {time_current}")
if weekday ==3:
    print(f"Today is Wednesday")
    print(f"the date is: {str(date_element)}")
    print(f"The time is: {time_current}")
if weekday ==4:
    print(f"Today is Thursday")
    print(f"the date is: {str(date_element)}")
    print(f"The time is: {time_current}")
if weekday ==5:
    print(f"Today is Friday")
    print(f"the date is: {str(date_element)}")
    print(f"The time is: {time_current}")
if weekday ==6:
    print(f"Today is Saturday")
    print(f"the date is: {str(date_element)}")
    print(f"The time is: {time_current}")
if weekday ==7:
    print(f"Today is Sunday")
    print(f"the date is: {str(date_element)}")
    print(f"The time is: {time_current}")
#end of tireshop code
print("")
#Get user info
tire_width = int(input("Enter the width of the tire in mm (Ex: 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (Ex: 60): "))
tire_diameter = int(input("Enter the diameter of the wheel in inches (Ex: 15): "))
print("")
#Restate info from user
print("You entered the following:")
print("")
print(f"Tire width: {str(tire_width)} Milimeters")
print(f"Aspect ratio: {str(aspect_ratio)}")
print(f"Tire diameter: {str(tire_diameter)} Inches")

#Ask if this is correct
question = input("Is this correct? ('Yes' or 'No'): ")
if question.lower() == "yes":
    #Equation time
    print("Preparing.")
    print("")
    #split into seperate parts
    n_divide = 10000000
    pi = 3.141592653589793238462643383279508
    d_multiplier = 2540
    #Keeping info
    # "v" is the volume in milliliters.
    # "pi" ratio of the circumference divided by the diameter of a circle (use math.pi).
    # "w" is the width of the tire in millimeters.
    # "a" is the aspect ratio of the tire.
    # "d" is the diameter of the wheel in inches.
    v_outside = (pi*tire_width**2 * aspect_ratio)
    #Now do parenethsis part
    v_inside = (tire_width * aspect_ratio + d_multiplier * tire_diameter)
    v_top = (v_outside * v_inside)
    volume = (v_top/n_divide)
    v_round = round(volume, 1)
    print(f"The volume is: {v_round} milliliters.")

elif question.lower() == "no":
    print("Try again.")

#Time to append 
import Volumes
volumeObject = open("Volumes.txt")
volumeObject.append(
    current_time, tire_width, aspect_ratio, tire_diameter, v_round     
)