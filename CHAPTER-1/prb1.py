#print the contents of a directory

import os

#directory
directory_path ='/'

contents=os.listdir(directory_path)

for item in contents:
    print(item)