"""
Group6_activity_4.py

Name of group members: Mohammad, Faisal, Khadija

GitHub Links:



Contribution of each member:

Mohammad: Docstrings and Comments

Faisal: 

Khadija: 

Describtion:
This program simulates an online shopping experience. 
You can view available items, add them to your cart, remove items, and check out. 
It calculates the total cost with discounts and taxes, providing a simple menu for these actions.

"""

import csv  # Import the CSV module to be able to read CSV files

class Article:  # Define a class named Article
    """
    Represents an article in the inventory
    """

    # Constructor to initialize the Article objects
    def __init__(self, name, inventory, price):  
        # Assigning attributes
        self.name = name 
        self.inventory = inventory 
        self.price = price 
    
    # Represent the class Article objects as a string
    def __str__(self):  
        return f"Article: {self.name}, Inventory: {self.inventory}, Price: ${self.price:.2f}"

class Cart:  # Define a class named Cart
    """
    Represents a shopping cart
    """

    # Constructor to initialize the Cart objects
    def __init__(self):  
        # Initialize an empty list for purchased items
        self.list_of_purchased = []  
    
    def addProduct(self, article, quantity):  
        """
        Adds an article to the shopping cart
        """

        for item in self.list_of_purchased:  # Loop through items in the cart
            if item.name == article.name:  # Check if the item is already in the cart
                item.inventory += quantity  # Increase the inventory if item is found
                return  # Exit
            
        # If item is not in cart, create a new Article object and add it to the cart
        self.list_of_purchased.append(Article(article.name, quantity, article.price))
    
    def removeProduct(self, article, quantity): 
        """
        Removes an article from the shopping cart
        """

        for item in self.list_of_purchased:  # Loop through items in the cart
            if item.name == article.name:  # Check if the item matches the one to remove
                if item.inventory <= quantity:  # If quantity to remove is greater than or equal to inventory:
                    self.list_of_purchased.remove(item)  # 1. Remove the item from the cart
                else:
                    item.inventory -= quantity  # 2. Reduce the inventory
                return  # Exit
    
    def displayCart(self):  
        """
        Displays the contents of the shopping cart
        """

        if not self.list_of_purchased:  # Check if the cart is empty
            print("Shopping cart is empty.")  
        else:
            for item in self.list_of_purchased:  # Loop through items in the cart
                print(item)  
    
    def checkout(self):  
        """
        Calculate the total cost of items in the cart
        """

        total = 0  # Initialize total cost
        for item in self.list_of_purchased:  # Loop through items in the cart
            if item.inventory >= 3:  # If inventory is 3 or more, apply a discount
                total += item.price * item.inventory * 0.9  # Calculate discounted price
            else:
                total += item.price * item.inventory  # Calculate regular price
        total *= 1.07  # Apply tax
        self.list_of_purchased.clear()  # Clear the cart after checkout
        return total  # Return the total cost

def read_data(file_path):  
    """
    Reads the inventory data from a CSV file
    """

    INVENTORY = {}  # Initialize an empty dictionary for inventory data
    try:
        with open(file_path, 'r') as file:  # Open the CSV file in read mode
            reader = csv.DictReader(file)  # Create a CSV reader object
            for row in reader:  # Loop through rows in the CSV file
                name = row['name']  # Get the name from the CSV row
                inventory = int(row['inventory'])  # Get the inventory from the CSV row and convert them to integer
                price = float(row['price'])  # Get the price from the CSV row and convert them to float
                INVENTORY[name] = Article(name, inventory, price)  # Create Article object and add to inventory
     # Handle file not found error
    except FileNotFoundError: 
        print("Error: The file path provided does not exist.")
    # Handle data format error
    except ValueError:  
        print("Error: Data format error in the file.")
    return INVENTORY  # Return the inventory dictionary

def get_positive_integer(prompt):  
    """
    Gets a positive integer input from the user
    """

    while True:  # Infinite loop until a valid input is received
        try:
            value = int(input(prompt))  # Gets user input and converts it to a integer
            if value < 0:  # Checks if the input is negative
                print("Please enter a positive number.")  
            else:
                return value  # Return the value
            
        # Handle invalid input 
        except ValueError:  
            print("Invalid input. Please enter a valid number.")  

def main(): 
    INVENTORY = read_data('products.csv')  # Read the inventory data from CSV file
    if not INVENTORY:  # Checks if the inventory is empty
        print("Failed to load inventory. Exiting program.")  
        return
    cart = Cart()  # Create a new Cart object
    
    while True:  # While loop for menu and user interaction
        # Print menu options
        print("\nMenu:")  
        print("1. List all items in inventory")
        print("2. List items in shopping cart")
        print("3. Add an item to the shopping cart")
        print("4. Remove an item from the shopping cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("Enter your choice: ")  
        
        # Option to list all items in inventory
        if choice == '1':  
            for article in INVENTORY.values():  # Loop through inventory items and print details
                print(article)
        
        # Option to list items in shopping cart
        elif choice == '2':  
            cart.displayCart() # Display the cart items
        
        # Option to add an item to the cart
        elif choice == '3':  
            item_name = input("Enter the name of the item: ")  # Get item name from user
            if item_name in INVENTORY:  # Check if item is in inventory
                item = INVENTORY[item_name]  # Find the item from inventory
                quantity = get_positive_integer("Enter the quantity: ")  # Get quantity from user
                if quantity <= item.inventory:  # Check if the inventory is big enough
                    item.inventory -= quantity  # Decrease the inventory quantity
                    cart.addProduct(item, quantity)  # Add the item to cart
                else:
                    print("Not enough inventory for this item.")  
            else:
                print("Item not found in inventory.")  
        
        # Option to remove an item from the cart
        elif choice == '4':  
            item_name = input("Enter the name of the item to remove: ")  
            if item_name in INVENTORY:  # Checks if the item is in inventory
                item = INVENTORY[item_name]  # Takes the item from inventory
                quantity = get_positive_integer("Enter the quantity to remove: ")  # Get the quantity wished to be removed
                cart.removeProduct(item, quantity)
            else:
                print("Item not found in inventory.")  
        
        # Option to checkout
        elif choice == '5':  
            total_cost = cart.checkout()  # Call checkout to calculate the total cost
            print(f"Total cost: ${total_cost:.2f}") 
        
        # Option to exit the program
        elif choice == '6':  
            print("Thank you for shopping with us!") 
            break  # Exit the loop and end the program
        
        # Handle invalid choices
        else:  
            print("Invalid choice. Please try again.")  
        
        cont = input("Would you like to continue? (y/n): ")  
        if cont.lower() != 'y':  # Check if the user does not wish to continue
            print("Thank you for using the shopping system!")  
            break  # Exit the loop and end the program

if __name__ == "__main__":
    main()