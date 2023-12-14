"""
this file is meant for testing code snippets
"""
import pyperclip


# Caesar Cipher
def cypher_encrypt_decrypt(message, key, mode='encrypt'):
    # every possible symbol that can be encrypted
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # stores the encrypted/decrypted form of the message
    translated = ''

    # capitalize the string in message
    message = message.upper()

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.find(symbol)  # get the number of the symbol
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key

            # handle the wrap-around if num is larger than the length of the letters or less than zero
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # copy the encrypted/decrypted string to the clipboard
    pyperclip.copy(translated)

    # return the encrypted/decrypted string to the screen
    return translated

def main():
    message = input("Enter message: ")
    key = int(input("Enter key: "))
    mode = input("Enter mode: ")
    print(cypher_encrypt_decrypt(message, key, mode))

main()