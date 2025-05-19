# Use words.txt as the file name
fname = input("Enter File name: ")
try:
    fh = open(fname)
except:
    print("Error: File not found")
    quit()

for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)
fh.close()