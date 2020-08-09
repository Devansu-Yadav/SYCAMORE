import tkinter
from learningpython.morse2text import morse_text, text_morse

guide = """Type your message below in normal text or Morse code using '.','-' separating words by /  and letters by 
spaces"""
window = tkinter.Tk()
window.geometry("900x600")
window.title("Morse Code Translator")
window.configure(background='#00ced1')
guide_msg = tkinter.Message(window, text=guide, justify=tkinter.LEFT, font="5", fg="Red", bg="#7cfc00", bd="6")
guide_msg.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
text_box = tkinter.Text(window, height=7, width=100)
text_box.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


def print_msg():
    display = tkinter.Text(window, height=7, width=100)
    display.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
    #
    try:
        text = text_box.get("1.0", 'end-1c')
        #
        final_output = morse_text(text)
        display.insert(tkinter.END, final_output)

    except TypeError:
        error_alert = "Sorry,I don't understand that"
        display.insert(tkinter.END, error_alert)

    except IndexError:
        display.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)


submit = tkinter.Button(window, text="Submit", width=35, command=print_msg, bd='5', activebackground="Royal blue", font="7", fg='indigo')
submit.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
window.mainloop()
