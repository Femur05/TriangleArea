# Calculate Triangle
# Written by Trevor Brinkmann
# Warning: Area can return as negative in which case the triangle isn't possible.
import math # For pi and sin to work
def areaOfTriangleS():  # Triangle with all sides given.
    a = float(input("Please input side length a "))
    b = float(input("Please input side length b "))
    c = float(input("Please input side length c "))
    s = (a+b+c)/2   # s is semiperimeter
    areaS = (s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of a triangle is: " ,areaS)

def areaOfTriangleA():  #Triangle given two sides and angle
    height = float(input("Please input height of side "))
    length = float(input("Please input length of side "))
    x = float(input("Please input angle in degrees "))
    areaA = (height*length*math.sin(math.radians(x)))/2
    print("Area of the triangle is: " ,areaA)

print("****Select Option****")

print("1. Three Sides \n2. Two Sides and Angle")

choice=input("Enter choice: ")
if choice=='1':
    areaOfTriangleS()
if choice=='2':
    areaOfTriangleA()
print("Program completed \nHave a good day")