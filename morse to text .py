import time
import sys
from text import text_morse
error_alert = "Sorry,I don't understand that"
print("""Type your message below in normal text or Morse code using '.','-' separating words by 
word spaces and letters by / """)
print()
msg = input().lower()


def morse_text(msg):
    morse_code = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d",
        ".": "e", "..-.": "f", "--.": "g",
        "....": "h", "..": "i", ".---": "j", "-.-": "k",
        ".-..": "l", "--": "m", "-.": "n",
        "---": "o", ".--.": "p", "--.-": "q", ".-.": "r",
        "...": "s", "-": "t", "..-": "u",
        "...-": "v", ".--": "w", "-..-": "x", "-.--": "y",
        "--..": "z", "-----": "0",
        ".----": "1", "..---": "2", "...--": "3",
        "....-": "4", ".....": "5",
        "-....": "6", "--...": "7", "---..": "8",
        "----.": "9", ".......": " ",
        "--..--": ",", "..--..": "?"
    }
    output = ""
    try:
        if (msg[0] == ".") or (msg[0] == "-"):
            letters = msg.split("/")
            for letter in letters:
                output += morse_code.get(letter)
            print(output, end="")
        else:
            text_morse(msg, morse_code)
    except TypeError:
        # Displaying error message animation
        for i in range(len(error_alert)):
            time.sleep(0.07)
            sys.stdout.write(error_alert[i % len(error_alert)])
            sys.stdout.flush()
        print()


morse_text(msg)



