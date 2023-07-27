
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '.......'
}

def morse(ut,morse_dict):
    encoded = ""
    ut = ut.split(' ')
    for char in ut:
        for key, value in morse_dict.items():
            if char == value:
                encoded += key
    return encoded.capitalize()

def text(ut, morse_dict):
    encoded = ""
    for char in ut:
        if char.upper() in morse_dict:
            encoded += morse_dict[char.upper()]
        else:
            encoded += char.upper()
        encoded += " "
    return encoded

def main():
    to_continue = True
    while to_continue:
        convert_index = input("--* Morse to Text, Type 'M' \n--* Text or Morse, Type 'T'\n").lower()
        while convert_index != "m" and convert_index != "t":
            convert_index = input("Please Enter \n--* Morse to Text, Type 'M' \n--* Text or Morse, Type 'T'\n")

        if convert_index == "m":
            user_text = input("Type or Paste Your Morse Code: ")
            encoded = morse(user_text, morse_code_dict)
            print(encoded)

        elif convert_index == "t":
            user_text = input("Type or Paste Your Text Content: ")
            encoded = text(user_text, morse_code_dict)
            print(encoded)

        continue_program = input("\nPress 1 to Continue or Any Key To Exit:")
        if continue_program != '1':
            to_continue = False

print("Welcome to String/Morse Code Converter")
main()
