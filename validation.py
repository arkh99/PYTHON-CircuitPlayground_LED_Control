from adafruit_circuitplayground import cp

#initialize the variables to default values
red = 0
green = 0
blue = 255

#prompt the user for the three components of the color: red green and blue
#validate each component as an integer value between 0 and 255
loopofred = True
while(loopofred):
    try:
        red = int(input("enter number from 0 to 255 as red"))
        if red > 255 or red < 0:
            print("not in the range")
        else:
            loopofred = False
    except:
        print("invalid input")

loopofgreen = True
while(loopofgreen):
    try:
        green = int(input("enter number from 0 to 255 as green"))
        if green > 255 or green < 0:
            print("not int the range")
        else:
            loopofgreen = False
    except:
        print("invalid input")

loopofblue = True
while(loopofblue):
    try:
        blue = int(input("enter number from 0 to 255 as blue"))
        if blue > 255 or blue < 0:
            print("not in the range")
        else:
            loopofblue = False
    except:
        print("invalid input")
