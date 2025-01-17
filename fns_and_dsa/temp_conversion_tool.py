# Global variable to store the base conversion factors
conversion_factors = {"FAHRENHEIT_TO_CELSIUS": 5 / 9, "CELSIUS_TO_FAHRENHEIT": None}

def update_conversion_factors():
    """
    Updates the CELSIUS_TO_FAHRENHEIT factor in the global dictionary.
    This avoids hardcoding the conversion factor directly.
    """
    global conversion_factors
    conversion_factors["CELSIUS_TO_FAHRENHEIT"] = 1 / conversion_factors["FAHRENHEIT_TO_CELSIUS"]

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factors.
    """
    return (fahrenheit - 32) * conversion_factors["FAHRENHEIT_TO_CELSIUS"]

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factors.
    """
    return (celsius * conversion_factors["CELSIUS_TO_FAHRENHEIT"]) + 32

def main():
    """
    Main program to interact with the user for temperature conversion.
    """
    # Update conversion factors before starting
    update_conversion_factors()

    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")
        else:
            raise ValueError("Invalid temperature unit.")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid temperature and unit.")

if __name__ == "__main__":
    main()
