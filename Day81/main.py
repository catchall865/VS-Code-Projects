ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.','Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-','5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}

def translator(message):
        return ' '.join(ENGLISH_TO_MORSE[char] for char in message.upper())

if __name__ == '__main__':
    print('Enter a message to translate into Morse Code: \n')
    
    while True:
        user_input = input('Please use only letters and numbers: \n')
        if user_input is None:
            break
        try:
            print(translator(user_input))
        except KeyError:
            print('Your message contains invalid characters. Try again or press Enter to quit. \n')