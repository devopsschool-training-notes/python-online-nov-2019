import json
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directoryclea
print("Files in %r: %s" % (cwd, files))

if os.path.isfile('sample-programs/system/input.json'):
	print('The file does exist.')	
else:
	print('The file does not exist.')	


with open('sample-programs/system/input.json', 'r') as input:
	obj = json.load(input)
	with open('sample-programs/system/output.txt', 'w') as output:
		output.write(obj['name'] + "'s Hobbies:\n")
		for hobby in obj['hobbies']:
			output.write(hobby + "\n")
