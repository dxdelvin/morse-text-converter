# Morse Code Converter

This is a simple Python program that allows you to convert between Morse code and regular text.

## Usage

1. Run the program.
2. Choose the conversion type:
   - For Morse to Text, type 'M'.
   - For Text to Morse, type 'T'.

## Morse Code Dictionary

The program uses the following Morse code dictionary:

```python
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
```

## Functions

- `morse(ut, morse_dict)`: Converts Morse code to text.
- `text(ut, morse_dict)`: Converts text to Morse code.

## How to Run

1. Copy and paste the code into a Python environment.
2. Run the program.
3. Follow the instructions to convert between Morse code and text.

## Author

[Delvin Dsouza](https://github.com/dxdelvin)
