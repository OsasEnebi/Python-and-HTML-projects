list1 = [1, 2, 3, 4]
print(list1[0])
print(list1[-1])
print(len(list1))
clist1 = list1[:]
print(clist1)
print(list1, clist1)


numbers = [9, 8, 7, 6, 5, 8, 4, 9]
del numbers[-1]
del numbers[-2]
numbers.append(0)
numbers.append(0)
print(numbers)
numbers.reverse()
print(numbers)
for number in numbers:
    print(number)
print(sum(numbers))

countries = ['Portugal', 'Spain','Bolivia', 'Brazil']
for country in countries:
    print(country)
countries.append('Italy')
print(countries)
countries.remove('Bolivia')
print(countries)
print(countries[0:2])
print(countries[2:4])
