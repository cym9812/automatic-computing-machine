"""
Name: Yimeng Cai
username: ycai541
ID number: 455251836
Description: Calculates the surface area and volume of a right regular octagonal prism
"""
import math
print("*"*34)
print("  Right Regular Octagonal Prism")
print("Surface Area and Volume Calculator")
print("*" * 34)
print()
Base_edge = int(input("Base Edge: "))
Height = int(input("Height: "))
print()
Surface_Area = 8 * Base_edge * Height + 4 * (1 + math.sqrt(2)) * Base_edge ** 2
Surface_Area = round(Surface_Area, 3)
Volume = 2 * (1 + math.sqrt(2)) * Height * Base_edge ** 2
Volume = round(Volume, 3)
print("Surface Area: ", Surface_Area, sep="")
print("Volume: ", Volume, sep="")
