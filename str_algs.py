text = "hello, world"

def r(text):
    s = ''
    for letter in text:
        s = letter + s
    return s

print(text)
print(r(text))
