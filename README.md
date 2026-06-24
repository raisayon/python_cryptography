#Book : Practical Cryptography in Python - LEarning Correct Cryptography by Example Apress , Seth James Nielson

1.1) All of the code examples in this book are written using python3 and the third-party "cryptography" module.

1.2) Setting up environment
python3 -m venv cryptography
source cryptography/bin/activate
pip install cryptography
pip install gmpy2

2.1) Caesar's shifty Cipher
Example :
substitution technique with the shift distance set to 1
HELLO WORLD encodes to IFMMP XPSME

Exercise 1.1 SHIFT CIPHER ENCODER (shift_cipher_encoder.py)
Create a python program that encodes and decodes messages using the shift cipher described in this section.
The amount of shift must be configurable.

Step 1 : 
let's create a simple function for creating our substitution tables.For simplicity , we will create two Python dictionaries: 
one containing the encoding table and one creating the decoding table.we will only encode and decode uppercase ASCII letters.

Key Points to Remember
The dictionary must have characters as keys: subst should map original characters to their replacements

Case sensitivity: The function distinguishes between 'a' and 'A' - they're different keys

Unmapped characters remain unchanged: If a character isn't in the substitution dictionary, it passes through unchanged

Works with any string: Can encode any string, including spaces, punctuation, and special characters

The function is flexible - you can build substitution dictionaries for many purposes like:

(Simple ciphers,Text obfuscation,Character conversion,Data transformation)

In shift_cipher_encoder.py implementation, the encode function takes an incoming message and a substitution dictionary.For each letter in the message, we replace it if a substitution is available.Otherwise, we just include the character itself with no transformation (preserving spaces and punctuation)
The decode operation in shift_cipher_encoder.py is completely unnecessary , but we have included it to emphasize that encoding and decoding in a substitution cipher work exactly the same.Only the dictionary needs to change.These function are sufficient to build an application.

#shift cipher application
