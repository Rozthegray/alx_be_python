# daily_reminder.py

def daily_reminder():
    # Prompt user for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process the task based on priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."
        case _:
            print("Invalid priority level. Please choose high, medium, or low.")
            return

    # Modify the reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    elif time_bound == "no":
        reminder += " Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity. Please answer with yes or no.")
        return

    # Display the customized reminder
    print(f"Reminder: {reminder}")

# Call the function
if __name__ == "__main__":
    daily_reminder()
