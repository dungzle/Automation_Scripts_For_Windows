import glob
import os
import shutil
from datetime import date, datetime

def get_latest_file(folder_path):
	"""
		From the given folder path, return list of files which is added or updated in the current day
		Input: 
			folder_path: String
		Output:
			latest_file: list
	"""
	files = glob.glob(folder_path+'\\*')
	latest_file = []
	tmp = datetime.combine(date.today(), datetime.min.time()).timestamp()
	for f in files:
		if (os.path.getctime(f) > tmp):
			latest_file.append(f)
	return latest_file

# Move recent added files from folders in source_dir to target_dir
if __name__ == "__main__":
	source_dir = ['C:\\Users\\vietd\\Desktop\\Fortinet\\a',
				  'C:\\Users\\vietd\\Desktop\\Fortinet\\b',
				  'C:\\Users\\vietd\\Desktop\\Fortinet\\c']			  
	target_dir = 'C:\\Users\\vietd\\Desktop\\Fortinet\\target'
		
	latest_files = [get_latest_file(folder) for folder in source_dir]
	for folder_path,files in zip(source_dir,latest_files):
		for f in files:
			if f:
				shutil.move(os.path.join(folder_path,f), target_dir)