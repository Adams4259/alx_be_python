#Personal Daily Reminder

task = input("What task would you like to be reminded of daily? ")
priority = input("How important is this task? (high/medium/low): ").lower()
time_bound = bool(input("Is this task time-bound? (True/False): "))

#Process the inputs and provide a reminder message
#match-case statement to handle different priority levels
#Use a Match Case statement to react differently based on the task’s priority.
#Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.

match priority:
    case "high":
        reminder = f"Reminder: You have a HIGH priority task - '{task}'. Please complete it as soon as possible!"
    case "medium":
        reminder = f"Reminder: You have a MEDIUM priority task - '{task}'. Try to get it done soon."
    case "low":
        reminder = f"Reminder: You have a LOW priority task - '{task}'. You can do it at your convenience."
    case _:
        reminder = f"Reminder: You have a task - '{task}'. Please prioritize it accordingly."
if time_bound:
    reminder += " This task is time-bound, so make sure to complete it within the specified time."

#VPrint a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
#A message should be ‘that requires immediate attention today!’
print(reminder)

# End of daily reminder program