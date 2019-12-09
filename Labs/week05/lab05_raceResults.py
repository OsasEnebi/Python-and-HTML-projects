runners = []
times = []

for r in range(4):
    runner = input('Runner >> ')
    runners.append(runner)
print('Runners = ', runners)

for runner in runners:
    time = float(input('How long did ' + runner + ' take >> '))
    times.append(time)
print(times)

quickest_time = min(times)
for k in range(len(times)):
    if times[k] == quickest_time:
        print('The winner is: '+ runners[k])




