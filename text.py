word_space = 7 * '.'
letter_space = "/"


def text_morse(msg, dictionary):
    dict_list = []
    text_to_morse = {}
    for i in dictionary:
        dict_list.append([dictionary[i], i])
    for ch in dict_list:
        # Creating a dictionary with alphabets as key and its morse equivalent as value
        text_to_morse[ch[0]] = ch[1]
    text_output = ""
    for ch in msg:
        if ch == " ":
            text_output += text_to_morse.get(ch) + letter_space
        elif msg.index(ch) == len(msg) - 1:
            text_output += text_to_morse.get(ch)
        else:
            text_output += text_to_morse.get(ch) + letter_space
    if text_output[len(text_output) - 1] == '/':
        final_output = []
        new_output = ''
        for char in text_output[0:len(text_output) - 1]:
            final_output.append(char)
        for characters in final_output:
            new_output += characters
        print(new_output, end="")
    else:
        print(text_output, end="")