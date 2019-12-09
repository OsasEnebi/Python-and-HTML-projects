def read_nonempty_string(prompt):
    ok = False
    while not ok:
        s = input(prompt)
        if len(s) > 0:
            ok = True
        else:
            print("Please type something...")
    return s


def get_grade(mark):
    if mark >= 70:
        return 'H1'
    elif mark >= 60:
        return 'H21'
    elif mark >= 50:
        return 'H22'
    elif mark <= 40:
        return 'Fail'



def main():
    file_name = read_nonempty_string("What is the name of the file >> ")
    input_file = read_nonempty_string("What is the name of the input file>> ")
    open_file = open(file_name)
    open_input = open(input_file, 'w')

    for line in open_file:
        line = line.rstrip()
        mark = int(line)
        grade = get_grade(mark)
        print(line + "& - " + grade)


    open_file.close()
    open_input.close()

main()

