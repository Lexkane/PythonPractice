import subprocess


subprocess.run(['ls','-l'],stdpit=subprocess.PIPE)
pr=subprocess.Popen('sort',stdout=subprocess.PIPE,stdin=subprocess.PIPE)
for i in range(25):
	pr.stdin.write(f'{i}\n.encode())
	out,err=pr.communicate()
	print(out.decode())
	pr.terminate()
	