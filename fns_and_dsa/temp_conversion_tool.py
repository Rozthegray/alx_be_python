# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor for F to C conversion
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Factor for C to F conversion
FREEZING_POINT_FAHRENHEIT = 32  # Freezing point adjustment for Fahrenheit

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factors."""
    return (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factors."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_FAHRENHEIT

# User Interaction
def main():
    try:
        # Prompt the user to enter a temperature
        temperature_input = input("Enter the temperature to convert: ")
        
        # Ensure the input is numeric
        try:
            temperature = float(temperature_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # Prompt the user to specify the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == "C":
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        else:
            print("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

# Run the script
if __name__ == "__main__":
    main()
