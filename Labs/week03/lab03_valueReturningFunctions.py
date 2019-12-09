def get_names(fname, lname):
    return lname + ' ' + fname


def longest_string(string1, string2):
    if len(string1) < len(string2):
        print(string1, 'is the longest string')
    elif len(string2) > len(string1):
        print(string2, 'is the longest string')
    elif len(string1) == len(string2):
        print('')


def read_nonnegative_float(prompt):
    ok = False
    while not ok:
        try:
            number = float(input(prompt))
            if number >= 0:
                ok = True
            else:
                print("Non-negative numbers please...")
        except:
            print("Must be numeric...")
    return number


def read_nonempty_string(prompt):
    ok = False
    while not ok:
        s = input(prompt)
        if len(s) > 0:
            ok = True
        else:
            print("Please type something...")
    return s

def calculate_rectangle(width, height):
    return width * height


def display(area):
    print("The area is", area)


def get_grade(grade):
    grade = read_nonempty_string("What is your grade>> ")





def main02():
    height = read_nonnegative_float("Height of rectangle >>> ")
    width = read_nonnegative_float("Width of rectangle >>> ")
    area = calculate_rectangle(width, height)
    display(area)

def main():
    print(get_names('Osas', 'Enebi'))


main()
main02()
print(longest_string('adkdhg', 'dskjgkjsda'))
