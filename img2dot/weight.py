# this standalone script helps to edit the weight images

#import tkinter as tk
#import graphics


from graphics import *
from button import Button
from PIL import Image as PIL_Image


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
            top = y - img_height//2 + 1
            bottom = y + img_height//2 +1
            img_win = img_win.crop((left, top, right, bottom))
            file_weight="weight/"+title+"-weight.jpeg"
            img_win.save(file_weight, "jpeg")
            img_win.show()
            print("button save: saved to ",file_weight)
        else:
            cir1 = Circle(p, 20)
            cir1.setFill("black")
            cir1.draw(win)
            
            
    for i in range(30):
        p=win.getMouse()
        cir1 = Circle(p, 10)
        cir1.setFill("black")
        cir1.draw(win)
            #win.getMouse()
    win.close()

    
                 


main()
