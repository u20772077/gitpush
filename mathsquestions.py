#import js2py

from PIL import ImageTk, Image, ImageOps
#import socket
import tkinter as tk
from datetime import datetime
from time import sleep
import time
#import json
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait

now = datetime.now()




master = tk.Tk()
master.title("Whatsapp Bot")
width = 500
height = 700
canvas1 = tk.Canvas(master, width=width, height=height, relief='raised', bg='white')
canvas1.pack()
# load the .gif image file
# canvas1.create_line(15, 25, 200, 25)
canvas1.create_line(width / 2, 0, width / 2, height, dash=(4, 2))
canvas1.create_line(800, height / 2, 0, height / 2, dash=(4, 2))

cx = canvas1.canvasx(width / 2)
cy = canvas1.canvasy(height / 2)
cid = canvas1.find_closest(cx, cy)[0]
canvas1.itemconfigure(cid, fill="blue")

# canvas1.create_line(55, 85, 155, 85, 105, 180, 55, 85)
# canvas1.create_text(400, 10, fill="black", font="Times 20 italic bold",
#                  text="Whatsapp Bot")
gif1 =ImageTk.PhotoImage(Image.open('images/w.jpg'))
# gif2 = tk.PhotoImage(file='images/9022c3da331305796ded3dda4c619df0.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
#canvas1.create_image(400, 350, image=gif2)

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas1.create_image(width / 2, height / 2, image=gif1)


# label1 = tk.Label(master, text='Whatsapp Bot')
# label1.config(font=('helvetica', 14))
# canvas1.create_window(200, 25, window=label1)
def blueSelection(event=None):
    l1 = tk.Label(master,
                  text="Enter the Message ", bg="blue")
    l2 = tk.Label(master,
                  text="How many message do you want to send ?", bg="blue")
    l3 = tk.Label(master,
                  text="Enter the Phone Number ", bg="blue")

    canvas1.create_window(100, 250, window=l1)
    canvas1.create_window(150, 290, window=l2)
    canvas1.create_window(100, 330, window=l3)

    e1 = tk.Entry(master)

    e2 = tk.Entry(master)

    e3 = tk.Entry(master)

    canvas1.create_window(400, 250, window=e1)
    canvas1.create_window(400, 290, window=e2)
    canvas1.create_window(400, 330, window=e3)

    master.mainloop()