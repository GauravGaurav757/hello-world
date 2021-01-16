"""
This project will find
the C.I of the number
you want.

"""
print("This thing will find the C.I of your number and the can be very big also.")

print("\nDon't put 'Rupees' sign here.")
a=(input("Enter your Principle over here:"))

print("\nDon't put 'Percent' sign here.")
b=(input("Enter your Rate here:"))

print("\nDon't put 'Y' for year.")
c=(input("Enter your Year here:"))

d= float(a)*(1+float(b)//100)**float(c) #This here the value will find the C.I over here only

print("Here is the Amount of yous",d)

#It is ready


