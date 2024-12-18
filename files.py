# Python has functions for creating, reading, updating, and deleting files.

# open a file
myFile = open('myFile.txt', 'w')

# get some info
print('name: ', myFile.name)
print('is closed: ', myFile.closed)
print('opening mode: ', myFile.mode)

# write to file
myFile.write('I love python')
myFile.write('and chichi')
myFile.close()

# append to file
myFile = open('myFile.txt', 'a')
myFile.write(' I also love perro')
myFile.close()

# read from a file 
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)