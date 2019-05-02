from functools import reduce
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # GLOBAL VARIABLE
morse_dictionary = {'A': '. ---', 'B': '--- . . .', 'C': '--- . --- .', 'D': '--- . .', 'E': '.',
                    'F': '. . --- .', 'G': '--- --- .', 'H': '. . . .',  'I': '. .',
                    'J': '. --- --- ---', 'K': '--- . ---', 'L': '. --- . .', 'M': '--- ---',
                    'N': '--- .', 'O': '--- --- ---', 'P': '. --- --- .', 'Q': '--- --- . ---',
                    'R': '. --- .', 'S': '. . .', 'T': '---', 'U': '. . ---', 'V': '. . . ---',
                    'W': '. --- ---', 'X': '--- . . ---', 'Y': '--- . --- ---', 'Z': '--- --- . .',
                    '1': '. --- --- --- ---', '2': '. . --- --- ---', '3': '. . . --- ---', '4': '. . . . ---',
                    '5': '. . . . .', '6': '--- . . . .', '7': '--- --- . . .', '8': '--- --- --- . .',
                    '9': '--- --- --- --- .', '0': '--- --- --- --- ---', " ": '       '}  # GLOBAL VARIABLE


# Task 2.1 - Caesar Cipher


def encrypt_caesar_cipher(plaintext):
    return ''.join([letters[divmod(letters.index(x) + 3, 26)[1]] if x in letters else x for x in plaintext])


def decrypt_caesar_cipher(ciphertext):
    return ''.join([letters[divmod(letters.index(x)-3, 26)[1]]if x in letters else x for x in ciphertext])


# task 2.2 - Vigenère Cipher


def encrypt_vigenere_cipher(plaintext, keyword):
    return ''.join([letters[divmod(letters.index(x) + letters.index(y), 26)[1]] for x, y in zip(plaintext, keyword)])


def decrypt_vigenere_cipher(ciphertext, keyword):
    return ''.join([letters[divmod(letters.index(x) - letters.index(y), 26)[1]] for x, y in zip(ciphertext, keyword)])


# task 2.3 - Morse Code


def encrypt_morse_code(plaintext):
    return '   '.join(morse_dictionary[x] for x, y in zip(plaintext, morse_dictionary) if [morse_dictionary[y] == x])


def decrypt_morse_code(ciphertext):
    delim_text = list(ciphertext.split("             "))  # split input to words
    split_to_letters = list(x.split('   ') for x in delim_text)  # split words to letters
    # join all the inputs to one list, 7*space as delimiter
    y = reduce(lambda a, b: a + ['       '] + b, split_to_letters)
    return ''.join(list(morse_dictionary.keys())[list(morse_dictionary.values()).index(x)] if
                   x in morse_dictionary.values() else ' ' for x in y)


def main():   # this is the 'main' method

# 2.1 check
    str = "F1RST P0ST"
    print("str=                   ", str)
    print("encrypt_caesar_cipher= ", encrypt_caesar_cipher(str))
    print("decrypt_caesar_cipher= ", decrypt_caesar_cipher(encrypt_caesar_cipher(str)))
    print()
    print("--------------------------------------------------------------")
    print()
# 2.2 check
    str = "ATTACKATDAWN"
    str1 = "LEMONLEMONLE"
    print("Plaintext=    ", str)
    print("Key=          ", str1)
    print("Ciphertext=   ", encrypt_vigenere_cipher(str, str1))
    print("deCiphertext= ", decrypt_vigenere_cipher(encrypt_vigenere_cipher(str, str1), str1))
    print()
    print("--------------------------------------------------------------")
    print()

# 2.3 check

    print(encrypt_morse_code("F1RST P0ST"))
    print(decrypt_morse_code(encrypt_morse_code("F1RST P0ST")))



if __name__ == '__main__':
    main()
