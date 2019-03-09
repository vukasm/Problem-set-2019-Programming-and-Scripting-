#Margarita Vukas, 2019-03-09
#Program that takes a positive floating number as input and outputs an approximation of its square root.

#This will import math module.
import math
#Asking user to enter a positive floating number which will be tha value of f.
f=float(input("Please enter a positive number:"))
#Using math.sqrt module to calculate the square root of the number.
sqrtf=math.sqrt(f)
#Using round() method rounding the square root to only two decimals which is approximation of the full number.
sqrtf=round(sqrtf,2)

#Printing the result on the screen.
print ("The square root of", f, "is approx.", sqrtf)