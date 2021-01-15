from tkinter import *


window = Tk()
window.geometry("350x350")
window.title("Morse code translator")
window.resizable(0, 0)


def translate():
    encrypt = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
               'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
               '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
               '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/', '!': '-.-.--',
               '@': '.--.-.', '&': '.-...'}

    decrypt = {v: k for k, v in encrypt.items()}
    message = inputter.get()
    inputter.delete(0, END)
    if len([i for i in message if i != '-' and i != '.' and i != ' ' and i != '/']) != 0:
        return ' '.join(encrypt[i] for i in message.upper())
    else:
        return ''.join(decrypt[i] for i in message.split())


def copy_text():
    text = translate()
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(text)
    clip.destroy()


def dev_note():
    notes = Label(window, text="Made by Aadhithyan and Rohit", font="times 15")
    notes.place(x=0, y=300)
    contact = Label(window, text="Discord: SoulNinja#7777", font="times10")
    contact.place(x=0, y=325)


heading = Label(window, text="Morse Code Translator", font="times 20 bold")
heading.place(x=50, y=20)

inputt_heading = Label(window, text="Translator", font="times 15")
inputt_heading.place(x=130, y=70)

inputter = Entry(window, width=20)
inputter.place(x=90, y=100)

copy_to_clipboard = Button(
    window, text="copy translated", command=copy_text, font="times4")
copy_to_clipboard.place(x=95, y=140)

devNotes = Button(window, text="Dev Notes", command=dev_note, font="times4")
devNotes.place(x=107, y=200)

window.mainloop()
