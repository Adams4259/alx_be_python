# Implements a simple interface for managing a shopping list

shopping_list = []

# function to add an item to the shopping list
def add_item(item):
    shopping_list.append(item)
    return f'Item "{item}" added to the shopping list.'

# function to remove an item from the shopping list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        return f'Item "{item}" removed from the shopping list.'
    
# function to view/display the current shopping list
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Shopping List")
    print("4. Exit")


#main 
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            print(add_item(item))
        elif choice == '2':
            item = input("Enter the item to remove: ")
            print(remove_item(item))
        elif choice == '3':
            print("Current Shopping List:")
            for idx, item in enumerate(shopping_list, start=1):
                print(f"{idx}. {item}")
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


