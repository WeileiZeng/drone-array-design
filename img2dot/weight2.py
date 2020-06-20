#import tkinter as tk
#import graphics
from graphics import *
from PIL import Image as PIL_Image


def test(img_name,width,height):
    win = GraphWin('Hello', width, height)    
    im = Image(Point(width//2,height//2), img_name)
    im.draw(win)
    for i in range(30):
        p=win.getMouse()
        cir1 = Circle(p, 10)
        cir1.setFill("black")
        cir1.draw(win)

    # saves the current TKinter object in postscript format
    win.postscript(file="image.eps", colormode='color')

    # Convert from eps format to gif format using PIL
    #from PIL import Image as NewImage
    img = PIL_Image.open("image.eps")
    img.save("blank.gif", "gif")        
    win.close()



#import PIL
img_name="racecar.png"
img_name="boundary.jpeg"
img=PIL_Image.open(img_name)
width,height=img.size
if ( height > 600 ):
    print("too big")
    img = img.resize((width//2,height//2), PIL_Image.ANTIALIAS)
    width,height=img.size
img.save("tmp.gif")

img_name="tmp.gif"

test(img_name,width,height)

#show(img_name,width,height)
