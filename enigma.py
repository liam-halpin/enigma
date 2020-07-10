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

def shift_rotor(string, shift_value):
    output = ""
    for i in range(0, len(string)):
        c = string[i]
        code = ord(c)
        if ((code >= 65) and (code <= 90)):
            c = chr(((code - 65 + shift_value) % 26) + 65)
        output += c
    return output

def contains_numbers(string):
    return any(char.isdigit() for char in string)

"""
 configure()

 This function will configure the Enigma's settings:
    - The chosen rotors;
    - The chosen reflector;
    - The rotor starting positions;
    - The plugboard settings;

"""
def configure():
    print("Configuring the Engima...")

    # Choose rotors (3 from a set of 5):
    chosen_rotors, choices = [], []
    while len(chosen_rotors) != 3:
        choice = input("Choose a rotor (I, II, III, IV, V): ").upper()
        if choice in choices: print("Rotor already chosen!"); continue
        elif choice == "I": chosen_rotors.append(rotorI); choices.append(choice)
        elif choice == "II": chosen_rotors.append(rotorII); choices.append(choice)
        elif choice == "III": chosen_rotors.append(rotorIII); choices.append(choice)
        elif choice == "IV": chosen_rotors.append(rotorIV); choices.append(choice)
        elif choice == "V": chosen_rotors.append(rotorV); choices.append(choice)
        else: print("Invalid input!")
    
    # Assign chosen rotors and assigned notches
    # RotorA = Left, RotorB = Middle, RotorC = Right
    rotorA = rotors[choices[0]]
    rotorB = rotors[choices[1]]
    rotorC = rotors[choices[2]]
    rotorA_notch = rotor_notches[choices[0]]
    rotorB_notch = rotor_notches[choices[1]]
    rotorC_notch = rotor_notches[choices[2]]

    # Choose a reflector (UKW_B or UKW_C):
    chosen_reflector = ""
    while chosen_reflector == "":
        choice = input("Choose a reflector (B or C): ")
        if choice == "B": chosen_reflector = UKW_B
        elif choice == "C": chosen_reflector = UKW_C
        else: print("Invalid input!")

    # Choose a start position for each rotor
    ring_positions = ""
    while len(ring_positions) != 3:
        choice = input("Choice the start positions for each rotor: e.g. ABC  ")
        if len(choice) != 3 and (contains_numbers(choice)):
            print("Invalid input!")
        ring_positions = choice
    
    ring_settings = ""
    while len(ring_settings) != 3:
        choice = input("Choose the initial ring settings e.g. ABC  ")
        if len(choice) != 3 and (contains_numbers(choice)):
            print("Invalid input!")
        ring_settings = choice

configure()
