plaintext = input("Please enter a sentence:")
plaintext = plaintext.lower ()
newtext = ""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
shifted = ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e"]
for letter in plaintext:
    if letter in alphabet:
        newtext += shifted [alphabet.index(letter)]
else:
        newtext += letter
print(newtext)