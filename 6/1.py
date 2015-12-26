'''
i. Write python code to remove all empty files in a given path.
ii. Given a path, traverse the path and display all files and
subdirectories in each level till the deepest level. Also display
total number of files and subdirectories.
'''
import os

path=input()

for i in os.listdir(path):
	if os.path.isfile(os.path.join(path,i)) and os.path.getsize(os.path.join(path,i))==0:
		os.remove(os.path.join(path,i))
n_files=0
n_dirs=0

for root,dirs,files in os.walk(path):
	n_dirs+=len(dirs)
	n_files+=len(files)
	print(root)
	print(dirs)
	print(files)
print('N-dirs',n_dirs)
print('N-files',n_files)

