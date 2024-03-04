#Input command used to allow user to insert the following information 

#Name, Age, House number, Street name (in that order). This information will be stored as strings in variables shown below:

# Initialize variables
Name = ""
Age = ""
House_Number = ""
Street_Name = ""

# Validate name input
while not Name.strip():  # Checks if the input is not empty
    Name = input("Enter name here: ")

# Validate age input
while not Age.isdigit():  # Checks if the input is a positive integer
    Age = input("Enter age here: ")
    if not Age.isdigit():
        print("Please enter a valid age.")

# Validating the house number 
while not House_Number.isdigit(): 
        House_Number = input("Enter House Number here: ")
        if not House_Number.isdigit():
             print('Please enter a valid house number : n')

# Validating the street name
while not Street_Name.strip():
     Street_Name = input("Enter the streat name here: ")

#A single sentence containing these details will print out: This is {Name}. {Name} is {Age} years old and lives at house number {House_Number} on {Stree_Name}
print(f'This is {Name}. {Name} is {Age} years old and lives at house number {House_Number} on {Street_Name}')