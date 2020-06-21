# for image processing
from PIL import Image
#math.sqrt
#import math
#os.listdir()
import os

#define constant
red=(255,0,0)
black=(0,0,0)

# return relative positions of pixels inside a circle
def get_circle(dot_size):
    circle=[]
    for i in range(dot_size):
        for j in range(dot_size):
            if ( i*i +j*j < dot_size * dot_size):
                circle.append((i,j))
                circle.append((i,-j))
                circle.append((-i,j))
                circle.append((-i,-j))
    #remove the first 4 position for origin
    return circle[4:]


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

# get boundary
def pix2bin(pixelAccess,width,height):
    #pixels_list=[]
    # a typical value to compare to
    temp=64
    neutral=dist_rgb(temp,temp,temp)
    for i in range(width-1):
        pixels_row_list=[]
        for j in range(height-1):
            if ( dist_pixels(pixelAccess[i,j+1], pixelAccess[i,j]) > neutral ) or ( dist_pixels(pixelAccess[i+1,j], pixelAccess[i,j]) > neutral )  :
                #print(i,j)
                #boundary
                pixelAccess[i,j]=red
                #(255,0,0)
                #pixels_row_list.append(1)
            else:
                pixelAccess[i,j]=black
                #(0,0,0)
                #pixels_row_list.append(0)
        #pixels_list.append(pixels_row_list)
#    return pixels_list
    #fix the last line
    for i in range(width):
        pixelAccess[i,height-1]=black
    for j in range(height):
        pixelAccess[width-1,j]=black
        

def draw_dot(pixelAccess, row, col, dot_size_array):
    color1=(0,120,120)
    for ( i,j) in dot_size_array:
        try:
            pixelAccess[row+i,col+j]=color1
        except:
            pass            
def remove(pixelAccess, row, col, dot_distance_array):
#    temp=pixelAccess[row,col]
    # background color used to remove pixels
    color1=(0,0,0)
    for (i,j) in dot_distance_array:
        try:
            pixelAccess[row+i,col+j]=color1
        except:
            pass


    
def reduce(pixelAccess, pixelAccessWeight, width, height, dot_distance, dot_size):
    #according to the weight, there will be two different distance
    
    dot_distance_array=get_circle(dot_distance)
    dot_distance_array_big=get_circle(dot_distance*3//2)
    # reduce the distance
    for i in range(width-1):
        for j in range(height-1):
            #if it is a boundary, remove nearby pixels
            if ( pixelAccess[i,j][0] > 200):
#                print(i,j)
                if ( pixelAccessWeight[i,j][0] < 200):
                    remove(pixelAccess, i, j, dot_distance_array)
                else:
#                    print(i,j)
                    remove(pixelAccess, i, j, dot_distance_array_big)
                    
    #draw the dot/drone
def draw_dots(pixelAccess, width, height, dot_distance, dot_size):
    dot_size_array=get_circle(dot_size)    
    drone_count=0
    for i in range(width-1):
        for j in range(height-1):
            #if it is a boundary, remove nearby pixels
            if ( pixelAccess[i,j][0] > 200):
#                print(i,j)
                drone_count+=1
                draw_dot(pixelAccess, i, j, dot_size_array)
    print("drone count:\t",drone_count)

def convert(title,filename, dot_distance, dot_size,show_img):
    print("--------------------",filename,"-------------------")
    print("input file:\t",filename)
    file_raw="tmp/"+title+"-raw.jpeg"            # raw file in jpeg
    file_boundary="tmp/"+title+"-boundary.gif"   # boundary
    file_boundary_jpeg="tmp/"+title+"-boundary.jpeg"  #boundary
    file_dots="tmp/"+title+"-dots.jpeg"          #exact position
    file_drone="output/"+title+"-drone.jpeg"     #draw


    img = Image.open(filename)
    #resize if height > 600
    width,height=img.size
    max_height=600
    if (height > max_height):        
        img = img.resize((width*max_height//height,max_height))
        print("resized to",img.size)

    
    #convert to RGB mode and jpeg format
    rgbimg = Image.new("RGB", img.size)
    rgbimg.paste(img)

    rgbimg.save(file_raw)
    print("saved as\t",file_raw)

    #reopen and get bounday
    img = Image.open(file_raw)
    pix = img.load()
    width,height=img.size
    pix2bin(pix,width,height)
          
#    im2 = Image.new(img.mode, img.size)
#    im2.putdata(pix)
          
    if show_img : img.show()
    img.save(file_boundary)
    img.save(file_boundary_jpeg)
    print("boundary file:\t",file_boundary,"\t",file_boundary_jpeg)

    # get weight
    try:        
        file_weight="weight/"+title+"-weight.jpeg"
        #file_weight=file_boundary_jpeg
        img_weight=Image.open(file_weight)
        pixAccessWeight=img_weight.load()
        print("get weight file:",file_weight)
    except:
        #if it doesn't exist, use boundary file itself
        file_weight=file_boundary
        img_weight=Image.open(file_weight)
        pixAccessWeight=img_weight.load()
        print("no weight file")

        
    # reduce to dot array according to dot_distance
    reduce(pix, pixAccessWeight, width, height, dot_distance, dot_size)
    img.save(file_dots)
    print("dot file:",file_dots)
    if show_img :    img.show()
    draw_dots(pix, width, height, dot_distance, dot_size)
    if show_img :    img.show()


    img.save(file_drone)
    print("drone file:\t",file_drone)

#    a=input()

    
def main():
    print("========= This program convert a cartoon to a drone array =========")
    dir_input = "input"
    #distance between drones
    dot_distance = 8
    #size of a drone/dot
    dot_size=2
    print("dot_distance:\t",dot_distance)
    print("dot_size:\t",dot_size)    
    show_img=True

    # test
    if (True):
        title="bird"
        title="elephant"
#        title="propose"

#        file=title+".jpeg"
        file=title+".png"
        convert(title,dir_input+'/'+file,dot_distance, dot_size,show_img)
        return
        
    for file in os.listdir(dir_input):
        title='.'.join(file.split(".")[:-1])
        print(title,dir_input+'/'+file)
        convert(title,dir_input+'/'+file,dot_distance, dot_size,show_img)


main()
