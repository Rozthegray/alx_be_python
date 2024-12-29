# square_pattern.py

def draw_pattern():
    # Prompt user for the pattern size
    size = int(input("Enter the size of the pattern: "))

    # Validate the input to ensure it's a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Initialize row counter
    row = 0

    # Use a while loop to iterate through rows
    while row < size:
        # Use a for loop to print asterisks in the current row
        for _ in range(size):
            print("*", end="")
        # Move to the next line after finishing the current row
        print()
        row += 1

# Call the function
if __name__ == "__main__":
    draw_pattern()
