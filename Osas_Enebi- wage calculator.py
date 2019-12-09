# Osas Enebi
# Student no: R00167276
# Class: CO.COMP1D-Y
# Group - Y
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# Empty lists to store wages and user info
wages = []
user_info = []


# Prints out the heading
def print_heading():
    print("-" * 15)
    print("Processing wages")
    print("-" * 15)


# Prints out a line to separate output. Mainly for aesthetic purposes
def print_line():
    print("-" * 15)


# Reads name and age as input and stores them in a list
def read_data(user_info):
    name = input('Name >> ')
    age = int(input('Age >> '))
    user_info.append(name)
    user_info.append(age)
    return name, age


# Asks for wages as input and calculates the average
def average_wages(days): # Reads from the list of days
    for day in range(len(days)):
        wage = int(input('Enter wages for ' + days[day] + ' >> '))
        wages.append(wage) # Stores the wages in a list
    print('Wages = ', wages)
    total = sum(wages)
    average = total/len(days)
    print('Calculating')
    print_line()
    print('Total: ', total)
    print('Your average wages are:', average)
    wages.append(total)
    wages.append(average)
    return total, average


# Calls all the functions and prints out a neat user profile
def main():
    print_heading()
    read_data(user_info)
    average_wages(days)
    print_line()
    print('User profile')
    print_line()
    print('Name: ', user_info[0])
    print('Age: ', user_info[1])
    print('Total wages: ', wages[-2] )
    print('Average wages: ', wages[-1])


main()




