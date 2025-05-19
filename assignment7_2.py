#Ask for the file name
fname = input("Enter file name: ")

#try to open file, but stop if it doesn't exist
try:
    file = open(fname)
except:
    print("File cannot be found:", fname)
    quit()

#Set up two things: a counter for how many numbers we find, and a total to add them up
count = 0
total = 0 

#Look at each line in the file
for line in file:
#Check if the line starts with "X-DSPAM-Confidence:"
    if line.startswith("X-DSPAM-Confidence:"):
    #Find the colon (:) in the line
        colon_position = line.find(":")
    #Get the number after the colon and turn it into a decimal number
        number = float(line[colon_position + 1:])
    #Add the number to our total
        total = total + number 
    #Add 1 to our counter
        count = count + 1
    
#After checking all lines, calculate the average 
if count > 0:
    average = total/count
    print("Average spam confidence:", average)
else:
    print("No numbers found")
    
#CLose the file
file.close()