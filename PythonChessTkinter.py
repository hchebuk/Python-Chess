#Author: Kenny Nguyen
#Project: Chess in python for CIS 407
#Description: This file will be the start menu for the chess game.

import tkinter as tk

myheight = 600
mywidth = 400

root = tk.Tk()

canvas = tk.Canvas(root, height=myheight, width=mywidth)
canvas.pack()

#background = tk.PhotoImage(file='chessimage.png')
#background_label = tk.Label(root, image=background)
#background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='gray')
frame.place(relx=0.11, rely=0.1, relwidth=0.8, relheight=0.8)

title = tk.Label(frame, text="Python Chess!", bg="pink")
title.place(relx=0.4 ,rely='0')

oneplayerbutton = tk.Button(frame, text="Single Player", bg='black', fg='white')
oneplayerbutton.place(relx=0.40, rely=0.3)

twoplayerbutton = tk.Button(frame, text="Player vs Player", bg='black', fg='white')
twoplayerbutton.place(relx=0.4, rely=0.5)

exitbutton = tk.Button(frame, text="Exit Game", bg='black', fg='white')
exitbutton.place(relx=0.40, rely=0.7)

root.mainloop()