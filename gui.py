#!/usr/bin/env python
import tkinter as tk
from solver import *

BORDER_COLOR = '#eb9d2c'
BORDER_SIZE = 10
CANVAS_HEIGHT = 400
CANVAS_WIDTH = 400
CHARACTER_LIMIT = 10
FONT_FAMILY = 'Arial'
FONT_SIZE = 18
INPUT_HEIGHT = 52

def format_words(words: list[str]) -> str:
    str = ''
    for word in words[:-1]:
        str = str + word + '\n'

    return (str + words[-1])

def set_label_text(input: str):
    words = solve_jumble(input)

    if (not len(words)):
        label.config(text = 'No solutions found', fg = 'gray')
    else:
        label.config(text = format_words(words), fg = 'black')

def initial_state():
    entry.focus_set()
    label.config(text = 'Enter jumbled letters\nand click Solve', fg = 'gray')

def reset_gui():
    entry.delete(0, 'end')
    initial_state()

def character_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:CHARACTER_LIMIT])

root = tk.Tk()
root.title('Jumble Solver')
img = tk.PhotoImage(file = 'icon.png')
root.wm_iconphoto(True, img)

canvas = tk.Canvas(root, height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
canvas.pack()

contents_frame = tk.Frame(root, bg = 'white')
contents_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
contents_frame_width = contents_frame.winfo_width()
contents_frame_height = contents_frame.winfo_height()

input_frame = tk.Frame(contents_frame, bg = BORDER_COLOR, bd = BORDER_SIZE)
input_frame.place(relx = 0, rely = 0, relwidth = 1, height = INPUT_HEIGHT)

output_frame = tk.Frame(contents_frame,
                        bg = BORDER_COLOR,
                        bd = BORDER_SIZE,
                        width = contents_frame_width,
                        height = (contents_frame_height-INPUT_HEIGHT))
output_frame.pack(pady = (INPUT_HEIGHT - BORDER_SIZE, 0), fill = 'both', expand = 'true')

entry_text = tk.StringVar()
entry = tk.Entry(input_frame, font = (FONT_FAMILY, FONT_SIZE), textvariable = entry_text)
entry.place(relx = 0, relheight = 1, relwidth = 0.6)
entry_text.trace('w', lambda *args: character_limit(entry_text))

solve_button = tk.Button(input_frame,
                         text = 'Solve',
                         font = (FONT_FAMILY, FONT_SIZE),
                         command = lambda: set_label_text(entry.get()))
solve_button.place(relx = 0.62, relheight = 1, relwidth = 0.18)

reset_button = tk.Button(input_frame,
                         text = 'Reset',
                         font = (FONT_FAMILY, FONT_SIZE),
                         command = lambda: reset_gui())
reset_button.place(relx = 0.82, relheight = 1, relwidth = 0.18)

label = tk.Label(output_frame, font = (FONT_FAMILY, FONT_SIZE))
label.place(relwidth = 1, relheight = 1)

initial_state()

def main():
    root.mainloop()

if __name__ == '__main__':
    main()
