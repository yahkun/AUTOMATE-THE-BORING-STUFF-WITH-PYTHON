import os, re

# all file objects in pwd
files = os.listdir('.')

# pattern to target unwanted part of old filename
pattern = re.compile(r'^\d\d? ')

for file in files:
	new_name = re.sub(pattern, '', file)
	os.rename(file, new_name)
