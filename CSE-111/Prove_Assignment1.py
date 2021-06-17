#Welcome user
print("")

#import math
import math

print("Welcome to Mike's Tire Shop! To find the volume of your tire,")
print("enter the required information below.")

print("")
#Get user info
tire_width = float(input("Enter the width of the tire in mm (Ex: 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (Ex: 60): "))
tire_diameter = float(input("Enter the diameter of the wheel in inches (Ex: 15): "))
print("")
#Restate info from user
print("You entered the following:")
print("")
print(f"Tire width: {tire_width} Milimeters")
print(f"Aspect ratio: {aspect_ratio}")
print(f"Tire diameter: {tire_diameter} Inches")

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
