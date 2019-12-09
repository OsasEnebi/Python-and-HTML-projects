usernames = []
passwords = []

def check_file():
    with open('user_data.txt','r') as r:
        for lines in r:
            line = lines.split()
            username = line[0]
            password = line[1]
            usernames.append(username)
            passwords.append(password)
        print(usernames)
        print(passwords)


def login(passwords):
    user = input("Enter your username >> ")
    pw = input("Enter your password >> ")
    for i in range(len(passwords)):
        if user == usernames[i] and pw == passwords[i]:
            print('login successful')
    else:
        print('Incorrect username or password. Please try again')

def main():
    check_file()
    login(passwords)

main()









