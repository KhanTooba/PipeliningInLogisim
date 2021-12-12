import sys
import io
import subprocess

def add_encode(filename):
	data = []
	with open(filename, 'r') as infile:
		data = infile.readlines()
	newfilename = filename.split('.')[0] + '2.asm' 
	with open(newfilename, 'w') as outfile:
		data = [".encode " + x.strip() + '\n' if x.strip() and x.strip()[0] != '.' and x.strip()[0] != '/' else x for x in data if x.strip() != '' and x[:2] != '.p']
		outfile.write(''.join(data))
	return newfilename

filename = sys.argv[1]
executable = sys.argv[2]
filename = add_encode(filename)
proc = subprocess.Popen([executable, filename], stdout=subprocess.PIPE)

data = [line.strip().split()[-1][2:] for line in io.TextIOWrapper(proc.stdout, encoding="utf-8")]
data.append("90000000")

with open(filename.split('.')[0] , 'w') as outfile:
	outfile.write("v2.0 raw\n")
	for i in range(0, len(data), 16):
		cur = data[i:i+16]
		outfile.write(" ".join(cur) + '\n')

print("Created file", filename)
print("Created file", filename.split('.')[0] )

