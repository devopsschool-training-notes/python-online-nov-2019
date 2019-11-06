"""
# File Exist or not
# File Ops 
            Reading
            Writing
            Appending
            Deleting
"""
import json
import os

# f = open('myfile.txt')

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directoryclea
print("Files in %r: %s" % (cwd, files))

if os.path.isfile('live/myfile.txt'):
	print('The file does exist.')	
else:
	print('The file does not exist.')


# Create a file
# f = open("live/createfile.txt", "x")

"""
# Overwriting a file with a content
f = open('live/createfile.txt', 'w')
f.write('Overwrite existing data.')
f.flush()
"""

# Append a file with a content
f = open('live/createfile.txt', 'a')
f.write('\nAppend this text.')
f.flush()
f.close()

# read a file with a content
f = open('live/createfile.txt')
print(f.read())

os.remove('live/createfile.txt')