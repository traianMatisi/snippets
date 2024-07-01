# Encoder decoder - 100 days of python - day 8
# Author: Traian 20-6-24

# TODO: Make it keep the letters case or restore them
# TODO: Catch str int errors in direction input

import os
from snippets.Python.resources.logo_cypher import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    while True:
        print(logo)
        text = input("Type your message:\n").lower()
        shift = int(input("\nWARNING!\nMultiples of 26 will have shift 0\nType the shift number:\n")) % 26
        while True:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            if direction == "decode":
                shift *= -1
            if direction == "encode" or direction == "decode":
                break
        print(caesar(text, shift))
        while True:
            stay = input("Do you wanna stay and continue? [yes/no]\n")
            if "yes" in stay or "no" in stay:
                break
        if stay == "no":
            print("Thanks and goodbye!\nWkdqnv dqg jrrgebh!")
            break
        os.system('cls' if os.name == 'nt' else 'clear')
def caesar(text, shift, cipher_text = ""):
    for i in range(len(text)):
        if text[i] in alphabet:
            cipher_text += alphabet[alphabet.index(text[i]) + shift]
        else:
            cipher_text += text[i]
    return cipher_text
main()
