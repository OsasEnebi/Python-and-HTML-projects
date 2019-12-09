scores = [ 9, 8, 6, 7, 6 ]
judges = ["kim", "tim", "fin", "lynn", "wynn"]
total = 0
for num in scores:
    total = total + num
print(total)

avg = 0
for perc in scores:
    avg = total / len(scores)
print(avg)
highest = max(scores)
lowest = min(scores)

print(highest)
print(lowest)

for k in range(len(scores)):
    if scores[k] == lowest:
        print(judges[k])

for k in range(len(scores)):
    if scores[k] == 6:
        print(judges[k])

