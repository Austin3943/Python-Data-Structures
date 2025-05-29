#Ask for the file name
fname = input("Enter file name: ")

#Try to open file, but stop if it doesn't work
try:
    file = open(fname)
except:
    print("File not found: ", fname)
    quit()

#Split the line into a list of words
words = []
for line in file:
    line_words = line.split()
    for word in line_words:
    if word not in words:
        words.append(word)

#Sort and print the resulting list
words.sort()
print(words)
