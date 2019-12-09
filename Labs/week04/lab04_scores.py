def read_nonempty_alphabatical_string(prompt):
    something_is_wrong = True
    while something_is_wrong:
        s = input()
        if len(s) > 0:
            something_is_wrong = False
        else:
           print("Please type something...")
    return s


def get_score(team_name):
    baskets = int(input("How many baskets were scored by " + team_name + ' '))
    points = int(input("How many points were scored by " + team_name + ' '))
    return baskets, points


def calculate_total(baskets, points):
    return baskets * 3 + points


def determine_winning_team(team1, t1, team2, t2):
    if t1 < t2:
        print(team1, 'has scored more points')
    elif t2 > t1:
        print(team2, 'has scored more points')
    else:
        print("Draw")

def display_result(name):
    print('Winner: ', name)




def main():
    name_team1 = read_nonempty_alphabatical_string("Name team #1 >>> ")
    goals1, points1 = get_score(name_team1)
    total1 = calculate_total(goals1, points1)
    name_team2 = read_nonempty_alphabatical_string("Name team #2 >>> ")
    goals2, points2 = get_score(name_team2)
    total2 = calculate_total(goals2, points2)
    winning_team = determine_winning_team(name_team1, total1, \
                                          name_team2, total2)
    display_result(winning_team)


main()