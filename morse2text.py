def text_morse(msg, dictionary):
    dict_list = []
    letter_space = " "
    text_to_morse = {}
    text_output = ''
    for i in dictionary:
        dict_list.append([dictionary[i], i])
    for ch in dict_list:
        # Creating a dictionary with alphabets as key and its morse equivalent as value
        text_to_morse[ch[0]] = ch[1]
    for ch in msg:
        translation = ''
        if ch != '':
            for char in ch:
                if char == " ":
                    translation += text_to_morse.get(char) + letter_space
                elif ch.index(char) == len(ch) - 1:
                    translation += text_to_morse.get(char)
                else:
                    translation += text_to_morse.get(char) + letter_space

            text_output += translation + '\n'
    return text_output


def morse_text(text):
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
        "----.": "9", "/": " ",
        "--..--": ",", "..--..": "?"
    }
    output = ""
    if (text[0] == ".") or (text[0] == "-"):
        letters = text.split(" ")
        for letter in letters:
            output += morse_code.get(letter)
        return output
    else:
        msg = text.lower()
        message = msg.split(".")
        text_output = text_morse(message, morse_code)
        return text_output


