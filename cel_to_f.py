celcius=float(input("Enter the temperature in celcius:"))
def conv(c):
    f=((9/5)*c)+32
    return f
faren=conv(celcius)
print("The converted temperature:",faren)