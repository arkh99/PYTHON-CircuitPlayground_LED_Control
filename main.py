from adafruit_circuitplayground import cp

#define the blue color as a tuple
blue = (0,0,255)

#paste your code from part 1 below
#The number of leds to switch on is stored in the variable totalLeds
looping = True
while (looping):
    try:
        light = int(input("Which Light ? "))
        if light >= 1 and light <= 10:
            print("The light to trun on is", light)
            light = light - 1
            # light -= 1
            looping = False
        else:
            print("wrong input for light")
    except ValueError:
        print("Invalid input, Please enter a number")
#paste your code from part 1 above


print("switch {} leds on.".format(totalLeds))
while True:
    #Turn on the leds
    for i in range(totalLeds):
        cp.pixels[i]=blue
