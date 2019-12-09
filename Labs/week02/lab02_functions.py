#Various functions to print out the shape of a box

def straight_line():
    print("+", "-" * 10, "+", sep="")

def gappy_line():
    print("-", 10 * " ", "-", sep="")

def draw_box():
    straight_line()
    for k in range(3):
        gappy_line()
    straight_line()

def draw_nose():
    print("")


draw_box()
