def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius without explicitly defining FAHRENHEIT_TO_CELSIUS_FACTOR.
    
    Formula:
        Celsius = (Fahrenheit - 32) * (5 / 9)
    """
    return (fahrenheit - 32) * (5 / 9)

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit without explicitly defining CELSIUS_TO_FAHRENHEIT_FACTOR.
    
    Formula:
        Fahrenheit = (Celsius * (9 / 5)) + 32
    """
    return (celsius * (9 / 5)) + 32

def main():
    """
    Main program to interact with the user for temperature conversion.
    """
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
