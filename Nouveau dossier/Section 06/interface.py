#!/usr/bin/env python3
# coding:utf-8
import tkinter as tk


def dire_bonjour():
    print("Bonjour")


root = tk.Tk()
root.title("Mon titre")
root.geometry("1080x720")  # taille fenêtre
root.minsize(480, 360)  # taille minimale
root.config(background="#d4d4d4")  # arrière plan fenêtre

label = tk.Label(root, text="Mon label", font=("Arial", 35), bg="#000", fg="#fff")  # arrière-plan et avant-plan
label.pack(side=tk.TOP)  # position

entry = tk.Entry(root, bd=3)  # bord
entry.pack()

button = tk.Button(text="Cliquez moi", command=dire_bonjour)  # action après clic via command
button.pack()

root.mainloop()  # boucle principale
