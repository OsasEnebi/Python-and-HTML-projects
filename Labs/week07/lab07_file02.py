fruit = []
more_fruit = []
with open('fruit.txt', 'r') as f:
    for lines in f:
        line = lines.rstrip()
        fruit.append(line)
    print(fruit)
    length = len(fruit)
    print(length)

with open('fruit.txt', 'r') as f:
    with open('fruit.txt', 'a') as wf:
        for lines in f:
            line = lines.rstrip()
            more_fruit.append(line)
        more_fruit.sort()
        print(more_fruit)
        wf.write('\n')
        wf.write(str(more_fruit))
        f.close()
        wf.close()


