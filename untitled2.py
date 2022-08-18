from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import ttk
import os

root = Tk()
root.geometry("600x600")
root.configure(background = "black")

label_img = Label(root, bg = "white", highlightthickness = 5)
label_img.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label_direct = Label(root, bg = "black", fg = "white", text = "Direction : ")
label_direct.place(relx = 0.3, rely = 0.8, anchor = CENTER)

directs = ["Left", "Right", "Up", "Down"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = directs, textvariable = selectedval)

img_path = ""

def openImg():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes = [("Image Files", "*.jpg *.png *.gif *.jpeg *.jfif *.jpe")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    name = os.path.basename(img_path)
    formated_name = name.split('.')[0]
    root.title(formated_name)
    label_img["image"] = img
    img.close()
    
def rotateImg():
    global img_path
    direct = selectedval.get()
    
    if direct == "Left":
        im = Image.open(img_path)
        img = ImageTk.PhotoImage(im.rotate(270))
        print(img_path)
        label_img["image"] = img
        img.close()
        
    elif direct == "Right":
        im = Image.open(img_path)
        img = ImageTk.PhotoImage(im.rotate(90))
        print(img_path)
        label_img["image"] = img
        img.close()
        
    elif direct == "Up":
        im = Image.open(img_path)
        img = ImageTk.PhotoImage(im.rotate(180))
        print(img_path)
        label_img["image"] = img
        img.close()
        
    elif direct == "Down":
        im = Image.open(img_path)
        img = ImageTk.PhotoImage(im.rotate(0))
        print(img_path)
        label_img["image"] = img
        img.close()
        
dropdown.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    
open_btn = Button(root, text = "Open Image", bg = "Grey", fg = "white", font = ("Times New Roman", 15, "bold"), padx = 15, pady = 10, relief = SOLID, command = openImg)
open_btn.place(relx = 0.5, rely = 0.1, anchor = CENTER)

rotate_btn = Button(root, text = "Rotate Image", bg = "Grey", fg = "white", font = ("Times New Roman", 15, "bold"), padx = 15, pady = 10, relief = SOLID, command = rotateImg)
rotate_btn.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()