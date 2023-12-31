import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

#start of program
root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)


#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo 
logo_label.grid(column=1, row=0)

#instructions
inst = tk.Label(root, text="Select a PDF file on your computer to extract all it's text.",font="Raleway" )
inst.grid(columnspan=3, column=0, row=1)

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text,font="Raleway")
browse_text.set('Browse')

root.mainloop()
#End of Program