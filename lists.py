# A List is a collection which is ordered and changeable. Allows duplicate members.

# create list
numbers = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'grapes', 'pears']

# use a constructor
# numbers2 = list((1,2,3,4,5)) 

# print(numbers, numbers2)

print(fruits[1])

# get length
print(len(fruits))

# append to list
fruits.append('mangeos')

print(fruits)

# remove
fruits.remove('grapes')

# insert into postion
fruits.insert(2, 'Strawberries')

# cahnge value
fruits[0] = 'blueberries'

# remove with pop
fruits.pop(2)

# reverse the list
fruits.reverse()

# sort list
fruits.sort()

# reverse sort
fruits.sort(reverse=True)


print(fruits)