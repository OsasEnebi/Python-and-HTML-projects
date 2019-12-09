fruit = []
number = []
with open('fruit_inventory.txt','r') as f:
    for lines in f:
        line = lines.split()
        fruit_list = line[0]
        stock_level = line[1]
        fruit.append(fruit_list)
        fruit.sort()
        number.append(stock_level)
    print('fruit = ',fruit)
    print('number = ',number)
    f.close()

