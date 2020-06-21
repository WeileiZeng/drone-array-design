#import tkinter as tk
#import graphics
from graphics import *
from button import Button
from PIL import Image as PIL_Image




def open_img(win,img_name,width,height):
#    win = GraphWin('Assigen weight for a cartoon', width, height)    
    im = Image(Point(width//2,height//2), img_name)
    im.draw(win)
    for i in range(30):
        p=win.getMouse()
        cir1 = Circle(p, 10)
        cir1.setFill("black")
        cir1.draw(win)


    win.close()

def main():
    win_width, win_height=1200,600+40
    img_width,img_height=win_width, win_height
    win = GraphWin('Assigen weight for a cartoon', win_width, win_height)
    win_center=Point(win_width//2,600//2)
    button_open=Button(win, center=Point(40,win_height-20), width=60, height=30, label="Open file:")
    button_open.activate()

    textEntry = Entry(Point(160,win_height-20),20)
    title="bird"
    textEntry.setText(title)
    textEntry.draw(win)
    button_save=Button(win, center=Point(300,win_height-20), width=60, height=30, label="Save file")
    button_save.activate()
    img=None
    while (True):
        p = win.getMouse()
        if button_open.clicked(p):
#            print("button open")
            try:
                img.undraw()
                print("undraw ",file_boundary)
            except:
                pass            
#            img_name="tmp.gif"
            title=textEntry.getText()
            file_boundary="tmp/"+title+"-boundary.gif"
            print("open file:",file_boundary)

#            open_img(win,img_name,width,height)

            img = Image(win_center, file_boundary)
            img_width,img_height=img.getWidth(),img.getHeight()
            img.draw(win)
        elif button_save.clicked(p):

            # saves the current TKinter object in postscript format
            win.postscript(file=".image.eps", colormode='color')
            # Convert from eps format to gif format using PIL
            #from PIL import Image as NewImage
            img_win = PIL_Image.open(".image.eps")
            x,y=win_center.getX(),win_center.getY()
            left = x-img_width//2
            right = x+img_width//2
            top = y - 600//2 + 1
            bottom = y + 600//2 +1
            img_win = img_win.crop((left, top, right, bottom))
            file_weight="weight/"+title+"-weight.gif"
            img_win.save(file_weight, "gif")
            print("button save: saved to ",file_weight)
        else:
            cir1 = Circle(p, 10)
            cir1.setFill("black")
            cir1.draw(win)
            
            
    for i in range(30):
        p=win.getMouse()
        cir1 = Circle(p, 10)
        cir1.setFill("black")
        cir1.draw(win)
            #win.getMouse()
    win.close()

    
                 
#import PIL
title="elephant"
file_boundary="tmp/"+title+"-boundary.jpeg"  #boundary
file_weight="weight/"+title+"-weight.jpeg"
img_name="racecar.png"
img_name="boundary.jpeg"
img=PIL_Image.open(file_boundary)
width,height=img.size
if ( height > 600 ):
    print("too big")
    img = img.resize((width//2,height//2), PIL_Image.ANTIALIAS)
    width,height=img.size
img.save("tmp.gif")

img_name="tmp.gif"

#test(img_name,width,height)

#show(img_name,width,height)


main()
