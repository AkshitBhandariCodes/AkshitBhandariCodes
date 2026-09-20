import sys, re
for f in ['C:/Users/akshi/.gemini/antigravity-ide/brain/a204bed8-506d-420a-a148-b8f589047130/ascii_1.svg', 'C:/Users/akshi/.gemini/antigravity-ide/brain/a204bed8-506d-420a-a148-b8f589047130/ascii_2.svg']:
    with open(f, 'r') as file:
        content = file.read()
    content = re.sub(r'clip-path=\"url\(#c\d+\)\"', '', content)
    with open(f, 'w') as file:
        file.write(content)
