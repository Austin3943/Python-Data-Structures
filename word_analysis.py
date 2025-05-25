# word_analysis.py
# Practice with .get(): Count word frequencies and group by length

# Sample text (imagine this is from a file)
text = "the cat and the dog and the mouse are running and jumping"

# Dictionaries for counting and grouping
word_count = {}
length_groups = {}

# Process each word
for word in text.split():
    # Count word frequencies
    word_count[word] = word_count.get(word, 0) + 1
    
    # Group by length
    word_length = len(word)
    current_group = length_groups.get(word_length, [])
    current_group.append(word)
    length_groups[word_length] = current_group
    
# Print word frequencies
print("Word Frequencies:")
for word, count in word_count.items():
    print("{}: {}".format(word, count))
    
# Print words grouped by length
print("\nWords Grouped by Length:")
for length, words in length_groups.items():
    print("Length {}: {}".format(length, words))
