from PIL import Image
import math
#Uclidean distance from wikipedia page of 'color difference'
def dist_pixel(pixel):
    r,g,b=pixel
    return dist_rgb(r,g,b)
def dist_rgb(r,g,b):
#could also work for (L,a,b)
    return 2*r*r+4*g*g+3*b*b+r/2*(r*r-b*b)/256 #Uclidean distance
#    return 0.3*r+0.59*g+0.11*b  #greyscale

def dist_pixels(pixel1,pixel2):
    pixel=( abs(pixel1[0]-pixel2[0]),
            abs(pixel1[1]-pixel2[1]),
            abs(pixel1[2]-pixel2[2]),
    )
    return dist_pixel(pixel)

def pix2bin(pixelAccess,width,height):
    pixels_list=[]
    temp=64
    neutral=dist_rgb(temp,temp,temp)
    for i in range(width-1):
        pixels_row_list=[]
        for j in range(height-1):
            if ( dist_pixels(pixelAccess[i,j+1], pixelAccess[i,j]) > neutral ) or ( dist_pixels(pixelAccess[i+1,j], pixelAccess[i,j]) > neutral )  :
                #print(i,j)
                #boundary
                pixelAccess[i,j]=(255,1,1)
                pixels_row_list.append(1)
            else:
                pixelAccess[i,j]=(1,1,1)
                pixels_row_list.append(0)
        pixels_list.append(pixels_row_list)
    return pixels_list

def remove(pixelAccess, row, col, dot_distance, dot_size):
#    temp=pixelAccess[row,col]
    color1=(0,0,0)
    for i in range(0,dot_distance):
        for j in range(0,dot_distance):
            try:
                pixelAccess[row+i,col+j]=color1
            except:
                pass
            try:
                pixelAccess[row-i,col+j]=color1
            except:
                pass
            try:
                pixelAccess[row+i,col-j]=color1
            except:
                pass
            try:
                pixelAccess[row-i,col-j]=color1
            except:
                pass
    color1=(0,120,120)
    for i in range(0,dot_size):
        for j in range(0,dot_size):
            try:
                pixelAccess[row+i,col+j]=color1
            except:
                pass
            try:
                pixelAccess[row-i,col+j]=color1
            except:
                pass
            try:
                pixelAccess[row+i,col-j]=color1
            except:
                pass
            try:
                pixelAccess[row-i,col-j]=color1
            except:
                pass
#    pixelAccess[row,col]=temp
    
def reduce(pixelAccess, width, height, dot_distance, dot_size):
    for i in range(width-1):
        for j in range(height-1):
            if ( pixelAccess[i,j][0] > 200):
#                print(i,j)
                remove(pixelAccess, i, j, dot_distance, dot_size)

#def main():
if (True):
#    img = Image.open("crop.jpeg")
    img = Image.open("raw.jpeg")
    pix = img.load()
    width,height=img.size
    pix2bin(pix,width,height)

#    im2 = Image.new(img.mode, img.size)
#    im2.putdata(pix)
    img.show()
    img.save("boundary.jpeg")


    dot_distance = 10
    dot_size=3
    reduce(pix, width, height, dot_distance, dot_size)

    img.show()

    
    img.save("drone.jpeg")
#    a=input()

    

#main()
