#Ask for the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File not found: ", fname)
    quit()
    
#Count the lines starting with "From " and extract the second word
count = 0 
for line in fh:
    if not line.startswith("From "): continue #Check for "From " with a space
    words = line.split()
    if len(words) > 1:  #Ensure theres a second word
        print(words[1]) #Print the second word
        count += 1

#Print the total count of such lines
print("There were", count, "lines in the file with From as the first word")