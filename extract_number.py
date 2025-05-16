# Extracts a floating-point number from a string (Python Data Structures, Lesson 1)
text = "X-DSPAM-Confidence:    0.8475"
colon_pos = text.find(":")
number_str = text[colon_pos + 2:]
number = float(number_str)
print(number)