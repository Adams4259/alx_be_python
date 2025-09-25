# display the current date and time
from datetime import datetime
from datetime import timedelta

# variable to hold the current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# function to format and return the current date and time in a readable format
def display_current_datetime():
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return f"Formatted Date and Time: {formatted_datetime}"



# Calculate a future date by adding days to the current date
#User input for number of days to add

days_to_add = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(days_to_add):
    future_date = current_datetime + timedelta(days=days_to_add)
    return f"Future Date after adding {days_to_add} days: {future_date.strftime('%Y-%m-%d')}"
print(calculate_future_date(days_to_add))

