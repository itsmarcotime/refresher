# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['chi', 'marco', 'perro']

# simple for loop
# for i in people:
#     print(f'current person: {i}')

# break
# for i in people:
#     if i == 'marco':
#         break
#     print(f'current person: {i}')

# continue
# for i in people:
#     if i == 'marco':
#         continue
#     print(f'current person: {i}')

# range
# for i in range(len(people)):
#     print(people[i])


# for i in range(0, 11):
#     print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0

while count <= 10:
    print(f'count: {count}')
    count += 1
