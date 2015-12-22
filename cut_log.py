#Filename:Cut_Log.py
import sys
import os
import fnmatch
import Queue
def filter_type_files_path(root,pattern="*",single_level=False,yield_folder=False):
	
	patterns = pattern.split(";")
	for path,subdir,files in os.walk(root):
		if yield_folder:
			files.extend(subdir)
		files.sort()
		for name in files:
			for pattern in patterns:
				if fnmatch.fnmatch(name,pattern):
					#print os.path.join(path,name)
					yield os.path.join(path,name)
					break
			if single_level:
				break
				
def cut_100M(log):
	fileHandle = open(log,"r")
	content = fileHandle.read(100*1024*1024)
	count = 1
	while content:
		new_file = log+str(count)	
		with open(new_file,"w") as f:
			f.write(content)
		content = fileHandle.read(100*1024*1024)
		count += 1
	fileHandle.close()	
	
def main():
	cur_dir=os.getcwd()	
	print cur_dir
	for log_file in filter_type_files_path(cur_dir,pattern="*.txt;*.log",yield_folder=True):
		if os.path.getsize(log_file)>100*1024*1024:
			print log_file	
			cut_100M(log_file)
	
if 	__name__=="__main__":
	main()
	os.system("pause")
