with open('file2.csv','r') as file:
    content = file.read()
modified_content = content[:-1]  # Remove the last character
with open('file2_modified.csv','w') as file:
    file.write(modified_content)