ta=int(input("Enter the temperature in Celsius: "))
v=int(input("Enter the wind speed: "))

twc=13.12+(0.6215*ta)-(11.37*(v**0.16))+(0.3965*ta*(v**0.16))

print("With an outside temperature of {0:.1f} degrees Celsius and a wind speed of {1:.1f} kilometres per hour, the windchill temperature is {2:.2f} degrees Celsius".format(ta,v,twc))