import tkinter as tk

class Window(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.canvas=tk.Canvas(self.master,width=60,height=60)
        self.canvas.bind("<Button-1>", self.get_mouse)
        #self.draw_black(10,10)
#        main.mainloop()
    def draw_black(self, x, y):
        img_name=("black.png")
        img = tk.PhotoImage(file=img_name)
        self.canvas.create_image(0,0, anchor=tk.CENTER, image=img)      
        self.canvas.pack()
    
    def get_mouse(self, event):
        print( "clicked at",  event.x, event.y)
        self.draw_black( event.x, event.y)

def show(img_name,width,height):
    root=tk.Tk()
    w=Window(root)
    w.mainloop()
#    canvas = tk.Canvas(master = root, width = width, height = height)

#    canvas.pack()      
#    img = tk.PhotoImage(file=img_name)
#    canvas.create_image(0,0, anchor=tk.NW, image=img)
#    img_name=("black.png")
#    img = tk.PhotoImage(file=img_name)
#    canvas.create_image(0,0, anchor=tk.CENTER, image=img)      
#    canvas.pack()
    #root.mainloop()

from PIL import Image
img_name="racecar.png"
img_name="boundary.jpeg"
img=Image.open(img_name)
width,height=img.size
if ( height > 600 ):
    print("too big")
    img = img.resize((width//2,height//2), Image.ANTIALIAS)
    width,height=img.size
img.save("tmp.png")
img_name="tmp.png"

show(img_name,width,height)
