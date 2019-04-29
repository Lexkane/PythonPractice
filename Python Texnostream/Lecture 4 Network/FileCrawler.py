from glob import glob

glob('../*/*.ipynb)

for t in os.walk('../'):
	print(t)


for curr_dir,sub_dirs,files in os.walk('../'):
	for file in files:
		if file.endswith('.ipybb'):
			print(os.path.join(curr_dir,file))