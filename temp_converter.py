"""
Temperature Converter Script
This program converts temperatures between Celsius and Fahrenheit
"""

# Function to display welcome message with ASCII art thermometer
def display_welcome():
    """
    Displays a fancy welcome message with a thermometer ASCII art
    Uses multi-line strings (triple quotes) to create the art
    """
    # ASCII art thermometer - each line is part of the image
    thermometer = """
    ╔════════════════════════════════════════════════╗
    ║                                                ║
    ║        🌡️  TEMPERATURE CONVERTER 🌡️           ║
    ║                                                ║
    ║            ___                                 ║
    ║           |   |     100°C ─┐                  ║
    ║           |###|            │                  ║
    ║           |###|      75°C ─┤  Hot!            ║
    ║           |###|            │                  ║
    ║           |###|      50°C ─┤                  ║
    ║           |   |            │                  ║
    ║           |   |      25°C ─┤  Nice            ║
    ║           |   |            │                  ║
    ║           |   |       0°C ─┘  Cold!           ║
    ║           |   |                                ║
    ║          (     )                               ║
    ║          (  O  )                               ║
    ║           (   )                                ║
    ║            ‾‾‾                                 ║
    ║                                                ║
    ║   Convert temperatures between Celsius and    ║
    ║   Fahrenheit with ease!                       ║
    ║                                                ║
    ╚════════════════════════════════════════════════╝
    """
    # Print the thermometer art
    print(thermometer)
    # Add a pause effect (makes it feel more polished)
    print("\n" + "=" * 50)
    print("Ready to convert some temperatures!")
    print("=" * 50 + "\n")


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """
    Takes a temperature in Celsius and returns it in Fahrenheit
    Formula: F = (C × 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    """
    Takes a temperature in Fahrenheit and returns it in Celsius
    Formula: C = (F - 32) × 5/9
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


# Main function that runs the program
def main():
    """
    This is the main function that controls the program flow
    """
    # Call the welcome function to show the thermometer and message
    display_welcome()

    # This creates an infinite loop that keeps running until we break out of it
    while True:
        # Display menu options to the user
        print("\nWhat would you like to convert?")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit")

        # Get user's choice and store it in a variable
        choice = input("\nEnter your choice (1, 2, or 3): ")

        # If/else statements to handle different choices
        if choice == "1":
            # Ask for temperature input
            try:
                # Try to convert input to a float (decimal number)
                celsius = float(input("Enter temperature in Celsius: "))

                # Call our conversion function
                fahrenheit = celsius_to_fahrenheit(celsius)

                # Display the result (:.2f formats to 2 decimal places)
                print(f"\n{celsius:.2f}°C = {fahrenheit:.2f}°F")

            except ValueError:
                # This runs if the user enters something that's not a number
                print("Error: Please enter a valid number!")

        elif choice == "2":
            # Similar to option 1, but converts the other direction
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"\n{fahrenheit:.2f}°F = {celsius:.2f}°C")

            except ValueError:
                print("Error: Please enter a valid number!")

        elif choice == "3":
            # Exit the program with a nice goodbye message
            print("\n" + "=" * 50)
            print("Thanks for using the Temperature Converter!")
            print("Stay cool (or warm)! 🌡️")
            print("=" * 50)
            break  # This exits the while loop

        else:
            # This runs if user enters anything other than 1, 2, or 3
            print("\nInvalid choice! Please enter 1, 2, or 3.")

        # Add a separator line for readability
        print("-" * 50)


# This checks if the script is being run directly (not imported)
# If true, it calls the main function to start the program
if __name__ == "__main__":
    main()
