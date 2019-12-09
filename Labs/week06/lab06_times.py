time_taken = [32, 27, 23,26, 26, 18]
names = ["Ann", "Joe", "Pat", "Ken", "Ali", "Ger"]


def target_times(time_taken, names):
    for t in range(len(time_taken)):
         target_time = (time_taken[t] * 0.10) + time_taken[t]
         print('The target time for ' + names[t] + 'is ' , target_time)


def main():
    target_times(time_taken, names)

main()
