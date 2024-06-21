# Encoder decoder - 100 days of python - day 8
# Author: Traian 20-6-24

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    text = "hello, world!".lower()
    shift = 5

    print(text)
    text = encrypt(text, shift)
    print(text)
    text = decrypt(text, shift)
    print(text)

def encrypt(text, shift):
    cipher_text = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            cipher_text += alphabet[alphabet.index(text[i]) + shift]
        else:
            cipher_text += text[i]
    return cipher_text

def decrypt(text, shift):
    cipher_text = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            cipher_text += alphabet[alphabet.index(text[i]) - shift]
        else:
            cipher_text += text[i]
    return cipher_text

main()
