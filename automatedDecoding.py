# Function to score text based on common English letter frequencies

def score_text(text):
    # Frequencies of letters E,T,A,O,I,N on English
    frequencies = {
        'E': 12.02,
        'T': 9.06,
        'A': 8.17,
        'O': 7.51,
        'I': 6.97,
        'N': 6.75,
        'S': 6.33,
        'H': 6.09,
        'R': 5.99,
        'D': 4.25,
        'L': 4.03,
        'C': 2.78, 
    }
    score = 0
    total_letters = 0
    
    for char in text.upper():
        if char.isalpha():
            total_letters += 1
        if char in frequencies:
            score += frequencies[char]
    
    #Return 0 if text is empty to avoid division by zero
    if total_letters == 0:
        return 0
    
    return score / total_letters

#Function to decrypt using a specific shift
def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - start - shift) % 26 + start)
        else:
            plaintext += char  # Non-alphabetic characters are not changed
    return plaintext
           
#Main automated decoding function
def automated_decoding(ciphertext):
    best_shift = 0
    best_score = 0
    best_match = ""
    
    #Brute-force through all possible shifts (0-25)
    for shift in range(26):
        test_text = caesar_decrypt(ciphertext, shift)
        score = score_text(test_text)
        
        #Track the shift that yields the most English-like text
        if score > best_score:
            best_score = score
            best_shift = shift
            best_match = test_text

    return best_shift,best_match

#Example usage
if __name__ == "__main__":
    sample_cipher = "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
    shift, decoded_msg = automated_decoding(sample_cipher)
    
    print(f"Detected Shift: {shift}")
    print(f"Decoded Message: {decoded_msg}")