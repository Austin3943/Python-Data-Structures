name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Create a dictionary to store sender counts
counts = {}
for line in handle:
    if line.startswith("From "): #Look for lines starting with "From "
        words = line.split()
        if len(words) > 1: #Ensure there are enough words
            email = words[1] # The email is the second word
            counts[email] = counts.get(email, 0) + 1

# Find the email with the maximum count
max_count = 0
max_email = None
for email, count in counts.items():
    if count > max_count:
        max_count = count
        max_email = email

# Print the results
print(max_email, max_count)

# Close the file
handle.close()