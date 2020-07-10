alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Initialise Rotors:
rotorI = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotorII = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotorIII = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotorIV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotorV = "VZBRGITYUPSDNHLXAWMJQOFECK"

rotors = {"I": rotorI, "II": rotorII, "III": rotorIII, "IV": rotorIV, "V": rotorV}

# Initialise Rotor Notches:
rotorI_notch = "Q"
rotorII_notch = "E"
rotorIII_notch = "V"
rotorIV_notch = "J"
rotorV_notch = "Z"

rotor_notches = {"I": rotorI_notch, "II": rotorII_notch, "III": rotorIII_notch,
                 "IV": rotorIV_notch, "V": rotorV_notch}

# Initialise Reflectors:
UKW_B = {"A":"Y", "Y":"A", "B":"R", "R":"B", "C":"U", "U":"C", 
         "D":"H", "H":"D", "E":"Q", "Q":"E", "F":"S", "S":"F", 
         "G":"L", "L":"G", "I":"P", "P":"I", "J":"X", "X":"J", 
         "K":"N", "N":"K", "M":"O", "O":"M", "T":"Z", "Z":"T", 
         "V":"W","W":"V"}
UKW_C = {"A":"F", "F":"A", "B":"V", "V":"B", "C":"P", "P":"C",
         "D":"J", "J":"D", "E":"I", "I":"E", "G":"O", "O":"G", 
         "H":"Y", "Y":"H", "K":"R", "R":"K", "L":"Z", "Z":"L", 
         "M":"X", "X":"M", "N":"W", "W":"N", "Q":"T", "T":"Q",
         "S":"U", "U":"S"}


def configure():
    print("Configuring the Engima...")

    # Choose rotors (3 from a set of 5):
    chosen_rotors, choices = [], []
    while len(chosen_rotors) != 3:
        choice = input("Choose a rotor (I, II, III, IV, V): ")
        if choice in choices: print("Rotor already chosen!"); continue
        elif choice == "I": chosen_rotors.append(rotorI); choices.append(choice)
        elif choice == "II": chosen_rotors.append(rotorII); choices.append(choice)
        elif choice == "III": chosen_rotors.append(rotorIII); choices.append(choice)
        elif choice == "IV": chosen_rotors.append(rotorIV); choices.append(choice)
        elif choice == "V": chosen_rotors.append(rotorV); choices.append(choice)
        else: print("Invalid input!")
    
    # Choose a reflector (UKW_B or UKW_C):
    chosen_reflector = ""
    while chosen_reflector == "":
        choice = input("Choose a reflector (B or C): ")
        if choice == "B": chosen_reflector = UKW_B
        elif choice == "C": chosen_reflector = UKW_C
        else: print("Invalid input!")
    
configure()
