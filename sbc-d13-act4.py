text = "apple!grape.orange,banana!"
tokens = []
current_token = ''

for char in text:
    if char.isalnum():  
        current_token += char
    else:
        if current_token:
            tokens.append(current_token)
            current_token = ''
        if char != ' ':  
            tokens.append(char)

if current_token:
    tokens.append(current_token)

print(tokens)
