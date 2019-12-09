
names= ["mary" , "ann",  "ben" , "kate",   "emily" ]
ages = [4, 7, 9, 2, 1]


def get_overfives(names, ages):
    for a in range(len(ages)):
        if ages[a] > 5:
            print(names[a].title(), ages[a])

def main():
    get_overfives(names, ages)

main()
