#Partial Listing : Some Assembly Required
import string
#STRING MODULES CONTAINS
# Constants: Definitions like ascii_letters, digits, and punctuation are written directly in the Python source code .
# Utility Functions: Functions like capwords() are fully implemented in Python .
# Classes: The Formatter and Template classes are defined here . The Template class, for example, uses the re module for pattern matching .

def create_shift_substitutions(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n)%alphabet_size]
        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding,decoding

def encode(message, subst):
    print(f"subst type: {type(subst)}")  # Will show <class 'function'>
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher


def decode(message, subst):
    return encode(message, subst)

# Example 1: Simple Caesar-like substitution
substitution = {
    'a': 'x',
    'b': 'y',
    'c': 'z',
    'd': 'a',
    'e': 'b',
    'f': 'c'
}

# Example 2: Full alphabet substitution (ROT13 style)
rot13 = {
    'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r',
    'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
    'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
    'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
    'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'
}

# Example 3: Including uppercase letters
subst_full = {
    'a': '@', 'b': '8', 'c': '(', 'd': ')', 'e': '3',
    'f': '|=', 'g': '6', 'h': '#', 'i': '!', 'j': ']',
    'k': '|<', 'l': '1', 'm': '^^', 'n': '^/', 'o': '0',
    'p': '|*', 'q': '9', 'r': '®', 's': '$', 't': '7',
    'u': 'µ', 'v': '√', 'w': 'ω', 'x': '×', 'y': '¥', 'z': '2',
    'A': '4', 'B': '8', 'C': '¢', 'D': '∂', 'E': '€',
    'F': 'ƒ', 'G': '&', 'H': '#'  # etc...
}

message = "abc"
result = encode(message,rot13)
print(result)

# message = "abc"
# result = encode(message,create_shift_substitutions(3))
# print(result)

decode_result = decode(result,rot13)
print(decode_result)