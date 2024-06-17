# PYTHON-CircuitPlayground_LED_Control
This Python program allows users to interact with Circuit Playground by controlling its LEDs based on user input for light number and RGB color values.

Hardware Requirements: Requires Circuit Playground board.

Software Requirements: Uses the adafruit_circuitplayground library.

Features:

LED Control: Users can specify which LED (indexed from 1 to 10) on Circuit Playground to turn on.
RGB Color Customization: Users can input RGB values (from 0 to 255) to set the color of the LEDs on Circuit Playground.
Input Validation: Validates user input for light number and RGB color values to ensure they are within valid ranges.
Feedback: Provides feedback to the user about the validity of inputs and the action taken (e.g., which LED is turned on, color set).

Usage Instructions:

Run the program and follow the prompts to input the desired light number (1-10).
Input RGB values for customizing the LED color on Circuit Playground.
Functionality:

User Input Handling: Uses input() function and loops with exception handling to ensure valid input.
LED Control: Uses a while loop to continuously control the LEDs based on user inputs until valid values are received.
Color Output: Sets the RGB values for LED colors on Circuit Playground using the cp.pixels[i] method.

EX:
Setting specific LEDs to blue color.
Creating custom colors by adjusting RGB values.

Future Enhancements: Consider adding features like:

Pattern animations for LEDs.
Integration with more sensors on Circuit Playground.
Interactive modes based on sensor inputs.
