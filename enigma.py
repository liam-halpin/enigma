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

def count_occurrences(string):
    string = string.upper().split(" ")
    string = "".join([str(elem) for elem in string])
    occurrences = {char : string.count(char) for char in set(string)}
    return occurrences

def used_twice(input_dict):
    for key in input_dict:
        if (input_dict[key] > 1):
            return False
    return True

"""
 run()

 This function will configure the Enigma's settings:
    - The chosen rotors;
    - The chosen reflector;
    - The rotor starting positions;
    - The rotor settings
    - The plugboard settings;

 And then it will encode/decode the provided text

"""
def run():
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

    
    # Choose ring settings for each rotor
    ring_settings = ""
    while len(ring_settings) != 3:
        choice = input("Choose the initial ring settings e.g. ABC  ")
        if len(choice) != 3 and (contains_numbers(choice)):
            print("Invalid input!")
        ring_settings = choice

    # Compute offset settings for each rotor
    rotorA_offset = alphabet.index(ring_settings[0])
    rotorB_offset = alphabet.index(ring_settings[1])
    rotorC_offset = alphabet.index(ring_settings[2])

    # Adjust rotors based on initial positions
    rotorA = shift_rotor(rotorA, rotorA_offset)
    rotorB = shift_rotor(rotorB, rotorB_offset)
    rotorC = shift_rotor(rotorC, rotorC_offset)

    if rotorA_offset > 0: rotorA = rotorA[26 - rotorA_offset:] + rotorA[0:26 - rotorA_offset]
    if rotorB_offset > 0: rotorB = rotorB[26 - rotorB_offset:] + rotorB[0:26 - rotorB_offset]
    if rotorC_offset > 0: rotorC = rotorC[26 - rotorC_offset:] + rotorC[0:26 - rotorC_offset]
    
    # Choose the plugboard settings
    plugboard_settings = ""
    while (len(plugboard_settings) != 29):    # 10 pairs + 9 spaces
        plugboard_settings = input("Please chooes the plugboard settings e.g. (AT BS DE FM IR KN LZ OW PV XY): ")
        print(len(plugboard_settings))
        if (used_twice(count_occurrences(plugboard_settings)) == False):
            print("You have entered a letter more than once!")
            plugboard_settings = ""
            continue
    
    # Convert specified plugboard settings into a dictionary
    plugboard = plugboard_settings.upper().split(" ")
    plugboard_dict = {}
    for pair in plugboard:
        if len(pair) == 2:
            plugboard_dict[pair[0]] = pair[1]
            plugboard_dict[pair[1]] = pair[0]
    
    output_text = ""
    input_text = input("Please enter the text you wish to encode/decode: ")

    for letter in input_text:
        encrypted_letter = letter
         

run()