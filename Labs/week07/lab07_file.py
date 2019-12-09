fruit = []
more_fruit = []

with open('fruit.txt', 'r') as f:
    contents = f.readlines()
    fruit.append(contents)
    length = len(fruit)
    print(length)
    f.close()

with open('fruit.txt', 'r') as f:
    contents = f.readlines()
    more_fruit.append(contents)
    more_fruit.sort()
    more_fruit.upper()
    print(more_fruit)
    f.close()
    with open('fruit.txt', 'a') as f:
        f.writelines('\n')
        f.writelines(str(more_fruit))
        f.close()


