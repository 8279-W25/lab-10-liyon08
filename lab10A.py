import time
import board
import neopixel

# Morse code dictionary
morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3, auto_write=False)

# Function to blink the LEDs for dot or dash
def blink_leds(color, duration):
    pixels.fill(color)
    pixels.show()
    time.sleep(duration)
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(unit_time)  

# Prompt for unit time and sentence
unit_time = float(input("Enter unit length (0 to 1 seconds): "))
sentence = input("Enter a sentence: ").lower()

# Filter out unwanted characters
filtered_sentence = ''.join(ch for ch in sentence if ch in morse_code_dict or ch == ' ')

# Convert to Morse code list
morse_list = []
for word in filtered_sentence.split():
    for letter in word:
        morse_list.append(morse_code_dict[letter])
    morse_list.append('/')  

# Blink the Morse code
color = (255, 165, 0)  
for code in morse_list:
    if code == '/':
        time.sleep(unit_time * 7)  
    else:
        for symbol in code:
            if symbol == '.':
                blink_leds(color, unit_time)        
            elif symbol == '-':
                blink_leds(color, unit_time * 3)     
        time.sleep(unit_time * 3)  

print("Morse code display finished.")
