# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# create tuple
fruits = ('apples', 'oranges', 'grapes')
#fruits2 = tuple(('apples', 'oranges', 'grapes'))

# single value needs a comma
fruits2 = ('Apples',)

print(fruits[1])

# cant change value
#fruits[0] = 'pears'

# delete tuple
del fruits2 

# get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# create set
fruits_set = {'apples', 'oranges', 'mango'}

# check if in set
print('apples' in fruits_set)

# add to set
fruits_set.add('grape')

# remove from set
fruits_set.remove('grape')

# clear set
fruits_set.clear()

# delete set
del fruits_set


print(fruits_set)
