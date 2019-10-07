import math
radius=int(input("Enter the radius: "))
height=int(input("Enter the height: "))

volume=math.pi*((radius)**2)*height

surfArea=(2*math.pi*((radius)**2))+(2*math.pi*radius*height)

print("Volume of the cylinder is: "+str("{:.2f}".format(volume)))
print("Surface Area of the cylinder is: "+ str("{:.2f}".format(surfArea)))