# Encoder decoder - 100 days of python - day 8
# Author: Traian 20-6-24

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    #direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    #text = input("Type your message:\n").lower()
    text = "Hello".lower()
    #shift = int(input("Type the shift number:\n"))
    shift = 3
    print(text)
    #if direction == "encode":
    text = encrypt(text = text, shift = shift)
    print(text)
    #elif direction == "decode":
    text = decrypt(text = text, shift = shift)
    print(text)

def encrypt(text, shift):
    cipher_text = ""
    for i in range(len(text)):
        cipher_text += alphabet.index(text[i])
    text = cipher_text
    return text
def decrypt(text, shift):
    cipher_text = ""
    for i in range(len(text)):
        cipher_text += alphabet.index(text[i])
    text = cipher_text
    return text

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
main()
