# Adding Function in shift_cipher_encoder to take a substitution dictionary and create a string that shows the mapping.This allows us to print out our different tables created from different shift values.
#Partial Listing 

def printable_substitution(subst):
    #sort by sources character so things are alphabetized
    mapping = sorted(subst.items())
    
    #Then creates two lines: source above , target beneath
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(subst_letter for _, subst_letter in mapping)
    return "{}\n{}".format(alphabet_line,cipher_line)

def printable_substitution(rot13):
    #sort by sources character so things are alphabetized
    mapping = sorted(rot13.items())
    
    #Then creates two lines: source above , target beneath
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(rot13_letter for _, rot13_letter in mapping)
    return "{}\n{}".format(alphabet_line,cipher_line)