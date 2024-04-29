
import sikidom

print("This program calculates the volume of a cuboid.")

print("Please enter the size of the sides of the cuboid (in cm):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

cuboid = sikidom.teglatest(a, b, c)

volume = cuboid.volume()

print(f"Volume of cuboid: {volume} cm\u00B3")

