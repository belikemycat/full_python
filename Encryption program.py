import random,string
chars = " "+string.punctuation+string.digits+string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
print(f'Original one:{chars}')
print(f'Encrypted   :{key}')

userinput = input("Enter a message to encrypt: ")
encrypted_one = ""
for letter in userinput:
    index = chars.index(letter)
    encrypted_one += key[index]
print(f"Original {userinput}")
print(f"Encrypted {encrypted_one}")

encrypted_one = input("Enter a message to decrypt: ")
userinput=""
for letter in encrypted_one:
    index = key.index(letter)
    userinput += chars[index]
print(f'Encrypted one: {encrypted_one}')
print(f'Original one: {userinput}')