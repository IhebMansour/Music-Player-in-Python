from tkinter import *
import pygame
import os

root = Tk()
root.title('Music Player')
root.geometry("800x400")

pygame.mixer.init()

songlist = Listbox(root, bg="black", fg="white", width=100, height=150)
songlist.pack()

root.mainloop()