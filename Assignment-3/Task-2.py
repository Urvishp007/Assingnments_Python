'''Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
    o   Square root of the number
    o   Natural logarithm (log base e) of the number
    o   Sine of the number (in radians)'''
import math as ma
num = float(input("Enter a number: "))
print(f"Square root: {ma.sqrt(num)}")
print(f"Logarithm: {ma.log(num)}")
print(f"Sine: {ma.sin(num)}")