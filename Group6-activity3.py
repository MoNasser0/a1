"""
Group6-activity3.py

Name of group members: Mohammad, Faisal, Khadija

GitHub Links:


Contribution of each member:

Mohammad: Stage 1 and 4, Docstrings

Faisal: Stage 3 and main

Khadija: Stage 2 and main

Describtion:
This program helps you work with numbers in CSV files by loading, cleaning, sorting, and showing them in a simple way.

"""

import csv

# Stage 1: Load Data
def load_data(file_path):
    """
    Returns:
        tuple: A tuple containing the chosen column name and its values.
    """

    while True:
        try:
            # Try to open the file
            with open(file_path, 'r') as file:
                print("File exists.")
                print("Loading file...")
                print("File loaded successfully!")

                # Create a CSV reader object   
                reader = csv.reader(file)
                next(reader)  # Skip header row
                data = list(reader)  # Read data into a list of lists

                print("Loaded table:")
                # Print column indices and names
                for i in range(len(data[0])):
                    print(str(i + 1) + ". " + data[0][i])

                while True:
                    choice = input("Choose a column from the selection below to process:\n"
                                   "Branch / Product / Price / Units sold\nPlease choose a column: ")
                    if choice.lower() not in ['branch', 'product', 'price', 'units sold']:
                        print("Invalid input. Please try again.")
                    else:
                        break

            chosen_column_index = data[0].index(choice)
            chosen_column_values = []
            for row in data[1:]:
                chosen_column_values.append(row[chosen_column_index])
                
            print("Values from the chosen column:", chosen_column_values)
            print("\nData loaded successfully!")
            return choice, chosen_column_values

        except FileNotFoundError:
            print("File not found. Please enter a valid path.")
            return load_data(file_path)

# Stage 2: Clean and Prepare Data
def clean_and_prepare_data(data, column):
    """

    Parameters:
        data (list): The list of lists containing the data.
        column (str): The name of the column to clean and prepare.

    Returns:
        list: The cleaned and updated data.
    """

    # Check if conversion to numeric type is needed
    try:
        data[0].index(column)  # Check if the column exists in the data
    except ValueError:
        print("Column not found in data.")
        return data

    # Convert numerical values from string type if necessary
    for row in data[1:]:
        if row[data[0].index(column)].isdigit():
            row[data[0].index(column)] = float(row[data[0].index(column)])

    # Define replacement strategies
    print("Would you like to replace empty cells from the column with:")
    print("1. Maximum value from the column")
    print("2. Minimum value from the column")
    print("3. Average value from the column")
    while True:
        choice = input("Enter your choice: ").strip()
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please select 1, 2, or 3.")
        else:
            break

    # Calculate replacement value based on user's choice
    column_values = []
    for row in data[1:]:
        if row[data[0].index(column)].isdigit():
            column_values.append(float(row[data[0].index(column)]))

    if choice == '1':
        replacement_value = max(column_values)
    elif choice == '2':
        replacement_value = min(column_values)
    elif choice == '3':
        replacement_value = sum(column_values) / len(column_values)

    # Replace empty values with the selected replacement strategy
    for row in data[1:]:
        if row[data[0].index(column)] == '':
            row[data[0].index(column)] = str(replacement_value)

    print("All empty values replaced with (based on your selection):", replacement_value)
    cleaned_data = [row[data[0].index(column)] for row in data]
    print(cleaned_data)

    return data

# Stage 3: Analyse Data
def analyze_data(numerical_data):
    """
    This function analyzes and sorts numerical data.

    Parameters:
        numerical_data (list): List of numerical values to analyze.

    Returns:
        list: Sorted numerical data.
    """

    if not numerical_data:
        print("No data to analyze.")
        return []

    print("Please choose if you want to sort the column in:")
    print("1. Ascending order")
    print("2. Descending order")
    while True:
        choice = input("Please enter your choice: ")
        if choice not in ['1', '2']:
            print("Invalid choice. Please select 1 or 2.")
        else:
            break

    sorted_data = sorted(numerical_data, reverse=(choice == '2'))
    if choice == '2':
        print("Column values are sorted in descending order!")
    else:
        print("Column values are sorted in ascending order!")

    print(sorted_data)
    return sorted_data

# Stage 4: Visualise Data
def visualize_data(column_name, column_values):
    """
    Parameters:
        column_name (str): The name of the column being visualized.
        column_values (list): List of numerical values to visualize.
    """

    print("Column:", column_name)
    print("Legend: each '*' represents 5 units\n")

    # Display the visualization of the data
    for value in column_values:
        stars_count = int(value) // 5
        stars = '*' * stars_count
        print(stars)

    print("\nVisualization completed!")

def main():
    print("---------------------------------")
    print("Welcome to Data Analysis CLI")
    print("---------------------------------")
    print("Program stages:")
    print("1. Load Data")
    print("2. Clean and prepare data")
    print("3. Analyze Data")
    print("4. Visualize Data")

    # Stage 1: Load Data
    print("Stage 1: Load Data\n")
    file_path = input("Please enter the path to the CSV file: ")
    numerical_data = load_data(file_path)

    # Stage 2: Clean and Prepare Data
    print("Stage 2: Clean and Prepare Data\n")
    cleaned_data = clean_and_prepare_data(numerical_data[1], numerical_data[0])

    # Stage 3: Analyse Data
    print("Stage 3: Analyse data\n")
    sorted_data = analyze_data(cleaned_data)

    # Stage 4: Visualise Data
    print("Stage 4: Visualise Data\n")
    visualize_data(numerical_data[0], sorted_data)

    print("\nThank you and good bye!")

if __name__ == "__main__":
    main()