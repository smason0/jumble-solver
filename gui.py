#!/usr/bin/env python
from tkinter import *
from solver import *

BORDER_COLOR = '#eb9d2c'
BORDER_SIZE = 10
BUTTON_RELWIDTH = 0.18
BUTTON_RELXPAD = 0.02
CANVAS_HEIGHT = 400
CANVAS_WIDTH = 400
CHARACTER_LIMIT = 10
ENTRY_RELWIDTH = 0.6
FONT_FAMILY = 'Arial'
FONT_SIZE = 18
INPUT_HEIGHT = 52
LABEL_COLOR = '#fbe9d0'

def format_words(words: list[str]) -> str:
    """Converts list of words to a formatted string."""
    str = ''
    for word in words[:-1]:
        str = str + word + '\n'

    return (str + words[-1])

def set_label_text(input: str):
    """Sets the text to display in the label widget."""
    words = solve_jumble(input)

    if (not len(words)):
        label.config(text = 'No solutions found', fg = 'gray')
    else:
        label.config(text = format_words(words), fg = 'black')

def initial_state():
    """Sets up the initial state of the GUI."""
    entry.focus_set()
    label.config(text = 'Enter jumbled letters\nand click Solve', fg = 'gray')

def reset_gui():
    """Resets the GUI back to initial state."""
    entry.delete(0, 'end')
    initial_state()

def character_limit(entry_text):
    """Enforces the character limit for text in the entry widget."""
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:CHARACTER_LIMIT])

root = Tk()
root.title('Jumble Solver')
img = PhotoImage(file = 'icon.png')
root.wm_iconphoto(True, img)

canvas = Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
canvas.pack()

contents_frame = Frame(root)
contents_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

input_frame = Frame(contents_frame, bg = BORDER_COLOR, bd = BORDER_SIZE)
input_frame.place(relx = 0, rely = 0, relwidth = 1, height = INPUT_HEIGHT)

output_frame = Frame(contents_frame,
                        bg = BORDER_COLOR,
                        bd = BORDER_SIZE,
                        width = contents_frame.winfo_width(),
                        height = (contents_frame.winfo_height() - INPUT_HEIGHT))
output_frame.pack(pady = (INPUT_HEIGHT - BORDER_SIZE, 0), fill = 'both', expand = 'true')

entry_text = StringVar()
entry = Entry(input_frame, font = (FONT_FAMILY, FONT_SIZE), textvariable = entry_text)
entry.place(relx = 0, relheight = 1, relwidth = ENTRY_RELWIDTH)
entry_text.trace('w', lambda *args: character_limit(entry_text))

solve_button = Button(input_frame,
                        text = 'Solve',
                        font = (FONT_FAMILY, FONT_SIZE),
                        command = lambda: set_label_text(entry.get()))
solve_button.place(relx = (ENTRY_RELWIDTH + BUTTON_RELXPAD),
                        relheight = 1,
                        relwidth = BUTTON_RELWIDTH)

reset_button = Button(input_frame,
                        text = 'Reset',
                        font = (FONT_FAMILY, FONT_SIZE),
                        command = lambda: reset_gui())
reset_button.place(relx = (ENTRY_RELWIDTH + BUTTON_RELWIDTH + 2*BUTTON_RELXPAD),
                        relheight = 1,
                        relwidth = BUTTON_RELWIDTH)

label = Label(output_frame, font = (FONT_FAMILY, FONT_SIZE), bg = LABEL_COLOR)
label.place(relwidth = 1, relheight = 1)

initial_state()

def main():
    root.mainloop()

if __name__ == '__main__':
    main()
