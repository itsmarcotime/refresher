# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create a dictionary
person = {
    'first_name': 'Marco',
    'last_name': ' Mata',
    'age': 26
}

#use constructor
# person2 = dict(fistname='chi', last_name='chi')

# get value
print(person['first_name'])
print(person.get('last_name'))

# add key value
person['phone'] = '555-555-5555'

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy dict
person2 = person.copy()
person2['city'] = 'San Antonio'

# remove item
del(person['age'])
person.pop('phone')

# clear
person.clear()

#get length
print(len(person2))

# list of dictionaries
people = [
    {'name': 'chichi', 'age': 700},
    {'name': 'kevin', 'age': 30}
]

print(people[1]['name'])