from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")
w.create_rectangle(20, 15, 100, 65, fill="red")

img_name=("black.png")
img = PhotoImage(file=img_name)
w.create_image(0,0, anchor=CENTER, image=img)

#w.binder("<Button-1>")
mainloop()
