import re

file_path = "E:\AI Diploma\Instant AI Diploma\Instant-AI-Diploma-\Session 11\File.txt"
with open(file_path, 'r') as file:
    content = file.read()

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
matches = re.findall(pattern, content)

# Print the matches
for match in matches:
    print(match)
