import os
import platform
folder_names=[] #generating empty list that contains list of all the names of folders.

#All images are in downloads/SUBDIRECTORY.
#Therefore, first we iterate through downloads folder where subdirectories exists. Then in the for loop inside we iterate through each
#folder to get file names.
for x in os.listdir('downloads'):
	folder_names.append(x)
	if platform.system()=='Windows':   #verify for windows operating systems
		directory = 'downloads\'+x 
	else:	
		directory = 'downloads/'+x 
	file_names=[] #generating empty list of file names of each subdirectory on every iteration.
	for y in os.listdir(directory):
		file_names.append(y)
	print(x+":\n")
	print(file_names)
