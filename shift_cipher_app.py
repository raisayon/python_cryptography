from printableSubstitution import printable_substitution 
from shift_cipher_encoder import create_shift_substitutions
if __name__ == "__main__":
    n=1
    encoding,decoding = create_shift_substitutions(n)
    while True:
        print("\nShift Encoder Decoder")
        print("-----------------------")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message")
        print("\t3. Decode Message")
        print("\t4. Change Shift")
        print("\t5. Quit.\n")
        choice = input(">> ")
        print()
        
        if choice == "1":
            print("Encoding Table:")
            print(printable_substitution(encoding))
            print("Decoding Table:")
            print(printable_substitution(decoding))
            
        
            
        else:
            print("Unknown option {}.".format(choice))