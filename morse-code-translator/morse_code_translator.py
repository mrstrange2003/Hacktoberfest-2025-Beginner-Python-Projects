# morse_code_translator.py
# Author: Madhavan Singh
# Description: Terminal-based Morse Code Translator (Text <-> Morse)

# Dictionary mapping letters/numbers to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Function to convert text to Morse code
def text_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)

# Function to convert Morse code to text
def morse_to_text(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(code, '') for code in morse.split(' '))

# Main program
def main():
    print("🔠 Morse Code Translator 🔠")
    while True:
        print("\nSelect option:")
        print("1. Text to Morse")
        print("2. Morse to Text")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            text = input("Enter text: ")
            print(f"Morse Code: {text_to_morse(text)}")
        elif choice == '2':
            morse = input("Enter Morse code (use '/' for spaces): ")
            print(f"Translated Text: {morse_to_text(morse)}")
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
