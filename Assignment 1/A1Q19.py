text=input("enter text")
punctuation = "!\"#$%&()*+, -./:;<=>?@[\]^_`{|}~"
no_punct = ""
for char in text:
    if char not in punctuation:
      no_punct += char
print(no_punct)