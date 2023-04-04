# Define the available primary colours as a tuple
PRIMARY_COLORS = ("red", "blue", "yellow")

# Define global variables for the secondary colours
PURPLE = "purple"
ORANGE = "orange"
GREEN = "green"

# Get the two primary colours from the user
color1 = input("Enter the first primary colour (red/blue/yellow): ").lower()
color2 = input("Enter the second primary colour (red/blue/yellow): ").lower()

# Check the validity of the user inputs
if color1 not in PRIMARY_COLORS:
    print(f"Error: Invalid {color1.capitalize()} color")
elif color2 not in PRIMARY_COLORS:
    print(f"Error: Invalid {color2.capitalize()} color")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:
    # Mixing two primary colours to get a secondary colour
    secondary_color = ""
    if (color1, color2) == (RED, BLUE) or (color2, color1) == (RED, BLUE):
        secondary_color = PURPLE
    elif (color1, color2) == (RED, YELLOW) or (color2, color1) == (RED, YELLOW):
        secondary_color = ORANGE
    elif (color1, color2) == (BLUE, YELLOW) or (color2, color1) == (BLUE, YELLOW):
        secondary_color = GREEN
    print(f"The new secondary colour is {secondary_color}")
