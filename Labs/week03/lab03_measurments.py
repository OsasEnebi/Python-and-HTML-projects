
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

def metres_to_km(m):
    return m / 1000

def metres_to_feet(m):
    return m * 3.28084

def metres_to_inches(m):
    return m * 39.3701

def check_if_valid(minimum, maximum, x):
    return minimum <= x <= maximum

def get_choice():
    menu = "1:Metres to Kilometres\n2:Metres to Feet\n3:Metres to Inches\n4:Quit"
    ok = False
    while not ok:
        try:
            number = int(input(menu))
            if check_if_valid(1, 4, number):
                ok = True
            else:
                print("Values 0-100 please...")
        except:
            print("Must be numeric...")
    return number

def process_choice():
    print('')

def main():
    print('')