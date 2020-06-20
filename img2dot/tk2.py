from tkinter import *

def callback(event):
    print( "clicked at", event.x, event.y)


root = Tk()      
canvas = Canvas(root, width = 300, height = 300)
canvas.bind("<Button-1>", callback)
canvas.pack()      
img = PhotoImage(file="racecar.png")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop() 



    
