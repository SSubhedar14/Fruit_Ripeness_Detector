from tensorflow.keras.models import load_model 
model= load_model('model_vgg16.h5')

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import keras
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import *
from tkinter import filedialog
image_size = 128
from PIL import Image, ImageTk
import numpy as np
import cv2
from os import listdir
from keras.preprocessing.image import img_to_array
import cv2


EPOCHS =2
INIT_LR = 1e-3
BS = 32
default_image_size = tuple((224, 224))
image_size = 0

width=224
height=224
depth=3


root = Tk()  # Main window 
f = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
root.title("Fruit Ripeness Detection")
root.geometry("1080x720")

canvas = Canvas(width=1080, height=250)
canvas.pack()
filename=('images.jpeg')
load = Image.open(filename)
load = load.resize((1200, 250), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
#photo = PhotoImage(file='landscape.png')
load = Image.open(filename)
img.place(x=1, y=1)
#canvas.create_image(-80, -80, image=img, anchor=NW)

root.configure(background='#FCFCE5')
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)




def click1( ):
	e2.delete("1.0","end-1c")
	filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("jpeg files","*.jpg"),("all files","*.*")) )
	#e1.delete('1.0', "end-1c")
	#e1.insert("end-1c", filename)
	load = Image.open(filename)
	load = load.resize((560,240), Image.ANTIALIAS)
	render = ImageTk.PhotoImage(load)
	img = Label(image=render)
	img.image = render
	img.place(x=250, y=349)

	# Load an image in PIL format
	imglist=[]
	image = cv2.imread(filename)
	image = cv2.resize(image, default_image_size)   
	img= img_to_array(image)

	imglist.append(img)
	np_image_list = np.array(imglist, dtype=np.float16) / 225.0
	preditcion=model.predict(np_image_list)
	preditcion=preditcion[0]
	print(preditcion)
	print(max(preditcion))
	pred=""
	# if max(preditcion) == 1.0:
	# 	pred = "Unripe Fruit"
	# else:
	# 	pred = "Ripe Fruit"

	if preditcion[0] > preditcion[1]:
		pred = "Ripe Fruit"
	else:
		pred = "Unripe Fruit"


	e2.insert("1.0",pred)




def clear_all():  # for clearing the entry widgets
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()




label1 = Label(root, text="Fruit Ripeness Prediction")
label1.config(font=('Italic', 18, 'bold'), justify=CENTER, background="#fdfe02", fg="#133e7c", anchor="center")
label1.pack(fill=X)


frame2.pack_forget()
frame3.pack_forget()

e2 = Text(frame2, width=40,height=1)
e2.grid(row=1, column=2,padx=10)


e1 = Text(frame1,height=15, width=70)
e1.grid(row=1, column=2, padx=10,pady=10)



button5 = Button(frame3, text="Predict",command=click1,width=20,height=1)
button5.grid(row=9, column=1, pady=10,padx=10)


frame2.configure(background="#b56727")
frame2.pack(pady=10)

frame1.configure(background="#b56727")
frame1.pack(pady=10)

frame3.configure(background="#b56727")
frame3.pack()

# f.configure(background="Submit")
# f.pack()

root.mainloop()

