#Drawing Patterns with nested loops

integer = int(input("Enter the size of the pattern: "))

#First, use a while loop to iterate through each row of the pattern.
#Inside the while loop, use a for loop to print asterisks (*) side by side without advancing to a new line (you can use print("*", end="") for this).
#After completing each row, print a newline character to move to the next row.
#Continue until the pattern forms a square of the inputted size.

while integer > 0:
    for i in range(integer):
        print("*", end="")
    print()  # Move to the next line after printing a row
    integer -= 1  # Decrease the size for the next row
# End of pattern drawing program