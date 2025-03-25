# Morse code dictionary for letters and numbers
morse_code_dict = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
    'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# Function to clean the sentence
def lower_sentence(sentence):
    return ''.join(ch for ch in sentence.lower() if ch in morse_code_dict or ch == ' ')

# Function to convert the cleaned sentence to a Morse code list
def convert_to_morse(sentence):
    morse_list = []
    words = sentence.split()
    for word in words:
        for letter in word:
            morse_list.append(morse_code_dict[letter])
        morse_list.append('/')  # Add '/' to indicate the end of a word
    return morse_list

# Function to display the Morse code list
def display_morse(morse_list):
    print("Morse Code List:")
    print(' '.join(morse_list))

# Main function
def main():
    sentence = input("Enter a sentence: ")
    cleaned = lower_sentence(sentence)
    morse_list = convert_to_morse(cleaned)
    display_morse(morse_list)

# Run the program
if __name__ == "__main__":
    main()
