# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Explicitly included as requested

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the formula:
    Celsius = (Fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the formula:
    Fahrenheit = (Celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to interact with the user for temperature conversion.
    """
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted:.2f}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted:.2f}°C")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid numeric temperature and unit.")
        print("Invalid temperature. Please enter a numeric value.")  # Explicitly added as requested

if __name__ == "__main__":
    main()
