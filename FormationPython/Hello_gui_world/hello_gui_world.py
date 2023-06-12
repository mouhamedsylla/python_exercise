import tkinter
from tkinter import BOTH

root = tkinter.Tk()
root.title("Hello Gui World")
root.iconbitmap('1.1 wave.ico')
root.geometry("400x400")
root.resizable(0, 0)

#Define fonts and colors
root_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"

root.config(bg=root_color)

#Define functions

#Define Layout
#Define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

#Create widgets
name = tkinter.Entry(input_frame, text="Enter your name", width=20)
submit_button = tkinter.Button(input_frame, text="Submit")
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

#Run root window's main loop
root.mainloop()