from printableSubstitution import printable_substitution 
from shift_cipher_encoder import create_shift_substitutions,encode,decode
import time

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
            
        elif choice == "2":
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(encode(message.upper(),encoding)))
         
        elif choice == "3":
            message = input("\nMessage to decode: ")
            print("Decoded Message: {}".format(decode(message.upper(),decoding)))
               
        elif choice == "4":
            new_shift = input("\nNew Shift (currently {}):".format(n))
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise ValueError("Shift must be greater than 0")
            except ValueError:
                print("Shift{} is not a valid number.".format(new_shift))
            else:
                n = new_shift
                encoding, decoding = create_shift_substitutions(n)
                
        elif choice == "5":
            print("Terminating.This program will self destruct in 5 seconds . \n")
            time.sleep(4)
            break
        
        else:
            print("Unknown option {}.".format(choice))