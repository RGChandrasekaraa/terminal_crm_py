import time

# Defining a User Function and Calling a Function
def greet_user(name):
    return f"Hello, {name}!"

# Parameters, Arguments, Multiple Parameters, and Multiple Arguments
def add_numbers(a, b):
    return a + b

# Creating a Function to Find the Maximum Value in a List
def find_maximum_value(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

# Returns, Multiple Returns
def min_max(numbers):
    min_value = numbers[0]
    max_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    return min_value, max_value

# Built-in Functions vs. User Defined Functions
def manual_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Activity: Output Prediction
def predict_output():
    a = 10
    b = 20
    return a + b

# Recap: Indentation and Execution Flow
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Introduction to Strings, Manipulation of Strings, Concatenating Strings
def concatenate_strings(str1, str2):
    return str1 + " " + str2

# Activity: Finding Length of a Combined String
def length_of_combined_string(str1, str2):
    combined = concatenate_strings(str1, str2)
    length = 0
    for char in combined:
        length += 1
    return length

# Strings are Immutable, Activity: Demonstrating String Immutability
def demonstrate_string_immutability(original):
    new_string = replace_string(original, "a", "o")
    return new_string

# Escape Characters
def demonstrate_escape_characters():
    return "This is a newline character: \nThis is a tab character: \tEnd of demo."

# Iterating Strings, Strings and Conditionals
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Formatting Methods
def format_string(name, age):
    return f"My name is {name} and I am {age} years old."

# Splitting Strings, Joining Strings
def manual_split(string, delimiter):
    parts = []
    temp = ''
    for char in string:
        if char == delimiter:
            parts.append(temp)
            temp = ''
        else:
            temp += char
    parts.append(temp)
    return parts

def manual_join(parts, delimiter):
    result = ''
    for i, part in enumerate(parts):
        result += part
        if i < len(parts) - 1:
            result += delimiter
    return result

# Strip Strings
def strip_string(string):
    start = 0
    end = len(string) - 1
    while start <= end and string[start] == ' ':
        start += 1
    while end >= start and string[end] == ' ':
        end -= 1
    return string[start:end+1]

# Replace Strings
def replace_string(original, to_replace, replacement):
    result = ''
    i = 0
    while i < len(original):
        if original[i:i+len(to_replace)] == to_replace:
            result += replacement
            i += len(to_replace)
        else:
            result += original[i]
            i += 1
    return result

# Find Strings
def find_string(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        match = True
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                match = False
                break
        if match:
            return i
    return -1

# Modules, Module Syntax
def module_demo():
    sqrt_16 = 16 ** 0.5  # Manually calculating square root
    return sqrt_16

# Python Standard Library: datetime, random
def datetime_demo():
    local_time = time.localtime()  # Get the local time
    year = local_time.tm_year
    month = local_time.tm_mon
    day = local_time.tm_mday
    hour = local_time.tm_hour
    minute = local_time.tm_min
    second = local_time.tm_sec
    formatted_time = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
    return formatted_time

def random_demo():
    seed = int(time.time()) % 10000  # Using current time as a seed for random number generation
    random_number = (seed * 9301 + 49297) % 233280
    return random_number

# Namespaces, Wildcard
def wildcard_demo():
    sqrt_25 = 25 ** 0.5  # Manually calculating square root
    return sqrt_25

# Decimals
def decimal_demo():
    return 10.5 + 0.5  # Simple float addition to simulate decimal addition

# Python Modules File and Scope
def scope_demo():
    global_var = "Global"
    def inner_function():
        local_var = "Local"
        return global_var, local_var
    return inner_function()

# Python Dictionary, Keys, Adding multiple Keys, Overwrite Values, Dictionary Comprehensions
def dictionary_demo():
    sample_dict = {"name": "John", "age": 30}
    sample_dict["address"] = "123 Main St"
    add_multiple_keys(sample_dict, ["city", "country"], "Unknown")
    sample_dict["age"] = 35
    comprehension = {k: v.upper() if isinstance(v, str) else v for k, v in sample_dict.items()}
    return sample_dict, comprehension

def add_multiple_keys(dictionary, keys, value):
    for key in keys:
        dictionary[key] = value

# Get an Invalid Key, Try/Except to Get a Key, Safely Get a Key
def safely_get_key(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default

# Delete a Key, Get all Keys, Iterate through all the Keys, Get all Values, Bonus: Get all Values, as a List, Get all Items
def delete_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]

def get_all_keys(dictionary):
    return list(dictionary.keys())

def get_all_values(dictionary):
    return list(dictionary.values())

def get_all_items(dictionary):
    return list(dictionary.items())

def iterate_keys(dictionary):
    for key in dictionary:
        print(f"Key: {key}")

def iterate_values(dictionary):
    for value in dictionary.values():
        print(f"Value: {value}")

def iterate_items(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

# Files, Reading a File (Activity), Notes on with keyword, Iterating Through Lines (Activity), Writing a File (Activity), Append to a File (Activity)
def read_customer_data(file_path):
    customers = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    data = manual_split(line.strip(), ',')
                    name = manual_split(data[0], ':')[1].strip()
                    age = int(manual_split(data[1], ':')[1].strip())
                    email = manual_split(data[2], ':')[1].strip()
                    phone = manual_split(data[3], ':')[1].strip()
                    customer = Customer(name, age, email, phone)
                    customers.append(customer)
    except FileNotFoundError:
        print("File not found. Please ensure the file path is correct.")
    return customers

def write_customer_data(file_path, customers):
    with open(file_path, 'w') as file:
        for customer in customers:
            line = f"name: {customer.name}, age: {customer.age}, email: {customer.email}, phone: {customer.phone}\n"
            file.write(line)

def append_customer_data(file_path, customer):
    with open(file_path, 'a') as file:
        line = f"name: {customer.name}, age: {customer.age}, email: {customer.email}, phone: {customer.phone}\n"
        file.write(line)

# Comma Separated Value (CSV) File, Reading a CSV File (Activity), Reading a CSV File (2) (Activity), Writing a CSV File (Activity)
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                data.append(manual_split(line.strip(), ','))
    return data

def write_csv(file_path, data):
    with open(file_path, 'w') as file:
        for row in data:
            line = manual_join(row, ',') + "\n"
            file.write(line)

# JavaScript Object Notation (JSON) File, Reading a JSON File (Activity), Writing a JSON File (Activity)
def read_json(file_path):
    data = ''
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data += line.strip()
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

# Activity (sample solution)
def sample_activity():
    return "Sample Activity Solution"

# Customer Class
class Customer:
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

# Utility Functions
def display_customers(customers):
    for customer in customers:
        print(f"Name: {customer.name}, Age: {customer.age}, Email: {customer.email}, Phone: {customer.phone}")

def add_customer(customers, name, age, email, phone):
    customers.append(Customer(name, age, email, phone))

def update_customer(customers, name, age, email, phone):
    for customer in customers:
        if customer.name == name:
            customer.age = age
            customer.email = email
            customer.phone = phone
            return
    print(f"Customer with name {name} not found.")

def delete_customer(customers, name):
    for customer in customers:
        if customer.name == name:
            customers.remove(customer)
            return
    print(f"Customer with name {name} not found.")

def find_max_age(customers):
    max_age = -1
    max_customer = None
    for customer in customers:
        if customer.age > max_age:
            max_age = customer.age
            max_customer = customer
    return max_customer

def concatenate_customer_info(customer):
    return f"{customer.name}, {customer.age}, {customer.email}, {customer.phone}"

def print_menu():
    print(r"""
     _____ _ _     _____ ____  __  __ 
    |  ___(_) |   | ____/ ___||  \/  |
    | |_  | | |   |  _|| |    | |\/| |
    |  _| | | |___| |__| |___ | |  | |
    |_|  |_|_|_____|_____\____||_|  |_|
    
    Welcome to cliCRM by 1839299!
    """)

def main():
    # Customer data
    customer_data = [
        "name: John Smith, age: 35, email: johnsmith@gmail.com, phone: 0413-535-124",
        "name: Jane Doe, age: 28, email: janedoe@yahoo.com, phone: 0401-655-568",
        "name: Bob Johnson, age: 42, email: bjohnson@hotmail.com, phone: 0433-515-912"
    ]

    # Writing sample data to the input file
    input_file = 'customer_data.txt'
    with open(input_file, 'w') as file:
        for line in customer_data:
            file.write(line + "\n")

    # Reading customer data from the file
    customers = read_customer_data(input_file)

    print_menu()

    while True:
        print("\nCustomer Relationship Management (CRM) System")
        print("1. Display Customers")
        print("2. Add Customer")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Find Customer with Maximum Age")
        print("6. Concatenate Customer Info")
        print("7. Find and Replace in Customer Name")
        print("8. Generate Random Customer ID")
        print("9. Get Current Date and Time")
        print("10. Calculate Total Customer Age")
        print("11. Find Maximum Age in Customer List")
        print("12. Find Minimum and Maximum Age in Customer List")
        print("13. Count Vowels in Customer Names")
        print("14. Format Customer String")
        print("15. Demonstrate String Immutability")
        print("16. Read Customer Data from CSV")
        print("17. Write Customer Data to CSV")
        print("18. Read Customer Data from JSON")
        print("19. Write Customer Data to JSON")
        print("20. Sample Activity")
        print("21. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_customers(customers)

        elif choice == '2':
            name = input("Enter name: ").strip()
            age = int(input("Enter age: ").strip())
            email = input("Enter email: ").strip()
            phone = input("Enter phone: ").strip()
            add_customer(customers, name, age, email, phone)
            write_customer_data(input_file, customers)
            print("Customer added successfully.")

        elif choice == '3':
            name = input("Enter name of the customer to update: ").strip()
            age = int(input("Enter new age: ").strip())
            email = input("Enter new email: ").strip()
            phone = input("Enter new phone: ").strip()
            update_customer(customers, name, age, email, phone)
            write_customer_data(input_file, customers)
            print("Customer updated successfully.")

        elif choice == '4':
            name = input("Enter name of the customer to delete: ").strip()
            delete_customer(customers, name)
            write_customer_data(input_file, customers)
            print("Customer deleted successfully.")

        elif choice == '5':
            max_age_customer = find_max_age(customers)
            if max_age_customer:
                print(f"Customer with the maximum age: {max_age_customer.name}, Age: {max_age_customer.age}")

        elif choice == '6':
            name = input("Enter name of the customer: ").strip()
            customer = next((customer for customer in customers if customer.name == name), None)
            if customer:
                print(f"Concatenated info: {concatenate_customer_info(customer)}")
            else:
                print(f"Customer with name {name} not found.")

        elif choice == '7':
            name = input("Enter name of the customer: ").strip()
            to_replace = input("Enter the substring to replace: ").strip()
            replacement = input("Enter the replacement string: ").strip()
            customer = next((customer for customer in customers if customer.name == name), None)
            if customer:
                customer.name = replace_string(customer.name, to_replace, replacement)
                write_customer_data(input_file, customers)
                print("Customer name updated successfully.")
            else:
                print(f"Customer with name {name} not found.")

        elif choice == '8':
            print(f"Generated random customer ID: {random_demo()}")

        elif choice == '9':
            print(f"Current date and time: {datetime_demo()}")

        elif choice == '10':
            total_age = manual_sum([customer.age for customer in customers])
            print(f"Total age of all customers: {total_age}")

        elif choice == '11':
            max_age = find_maximum_value([customer.age for customer in customers])
            print(f"Maximum age among customers: {max_age}")

        elif choice == '12':
            min_age, max_age = min_max([customer.age for customer in customers])
            print(f"Minimum age: {min_age}, Maximum age: {max_age}")

        elif choice == '13':
            name = input("Enter name of the customer: ").strip()
            customer = next((customer for customer in customers if customer.name == name), None)
            if customer:
                vowels_count = count_vowels(customer.name)
                print(f"Number of vowels in {customer.name}: {vowels_count}")
            else:
                print(f"Customer with name {name} not found.")

        elif choice == '14':
            name = input("Enter name: ").strip()
            age = input("Enter age: ").strip()
            print(format_string(name, age))

        elif choice == '15':
            original = "banana"
            new_string = demonstrate_string_immutability(original)
            print(f"Original string: {original}, New string: {new_string}")

        elif choice == '16':
            csv_file = input("Enter the CSV file path: ").strip()
            csv_data = read_csv(csv_file)
            print(f"CSV Data: {csv_data}")

        elif choice == '17':
            csv_file = input("Enter the CSV file path: ").strip()
            data = [[customer.name, customer.age, customer.email, customer.phone] for customer in customers]
            write_csv(csv_file, data)
            print("Customer data written to CSV file successfully.")

        elif choice == '18':
            json_file = input("Enter the JSON file path: ").strip()
            json_data = read_json(json_file)
            print(f"JSON Data: {json_data}")

        elif choice == '19':
            json_file = input("Enter the JSON file path: ").strip()
            data = '{"customers": [' + ', '.join([f'{{"name": "{customer.name}", "age": {customer.age}, "email": "{customer.email}", "phone": "{customer.phone}"}}' for customer in customers]) + ']}'
            write_json(json_file, data)
            print("Customer data written to JSON file successfully.")

        elif choice == '20':
            print(sample_activity())

        elif choice == '21':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
