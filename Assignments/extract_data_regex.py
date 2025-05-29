import re

#Sample text
text = "Contact us at support@example.com or sales@company.org. Our phone numbers are 123-456-7890 and 987.654.3210. Visit us at http://example.com for more info."

#Extract email addresses
emails = re.findall(r'\S+@\S+', text)
print("Emails found:", emails)

#Extract numbers
numbers = re.findall(r'\d+\.?\d*|\d+-\d+-\d+', text)
print("Numbers found:", numbers)

#Extract URLs
urls = re.findall(r'http\S+', text)
print("URLs found:", urls)
