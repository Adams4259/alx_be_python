# Multiplication Table
# This program prints the multiplication table from 1 to 10.

number = int(input("Enter a number to see its multiplication table: ")) 
print(f"Multiplication table for {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}") 

# End of multiplication table program