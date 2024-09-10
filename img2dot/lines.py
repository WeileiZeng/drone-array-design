# convert a graph into group of lines

import random

def sample(): # return a square lattice
    # size 30 by 30
    rows=3
    cols=3
    L = 10
    xy_list=[]
    for i in range(rows+1):
        row = 10*i
        for j in range(L*cols):
            col = j
            xy_list.append((row,col))

    # add vertical dots
    yx_list=[]
    for i in range(cols+1):
        col = 10*i
        for j in range(L*rows):
            row = j
            yx_list.append((row,col))
    xy_list.extend(yx_list)
    
    #random.shuffle(xy_list)
    return xy_list


def dist(p1,p2):  # distance between two points
    x1,y1=p1
    x2,y2=p2
    d = (x1-x2)**2 + (y1-y2)**2
    return d

def near(p1,p2):
    if dist(p1,p2)<2:
        print(f'near: {p1,p2}')
        return True
    return False

def in_the_line(xy,line):
    p_start=line[0]
    p_end=line[-1]
    if dist(xy,p_end) < 2:
        line.append(xy)
        return True
    elif dist(xy,p_start) < 2:
        line.reverse()
        line.append(xy)
        return True
    else:
        return False
        
def combine_lines(lines):
    #lines_new=[]
    length = len(lines)
    for i in range(length):
        index = length-1-i # the current line to look at
        line = lines[index]
        line_end = line[-1]
        line_start = line[0]
        for j in range(index):# go through all previous lines
            line1 = lines[j]
            line1_start = line1[0]
            line1_end = line1[-1]
            found_connected=True #assume true
            # join the two lines if connected
            if near(line1_end,line_start):
                line1.extend(line)
            elif near(line1_end,line_end):
                line.reverse()
                line1.extend(line)
            elif near(line1_start,line_start):
                line1.reverse()
                line1.extend(line)
            elif near(line1_start,line_end):
                line_new = line.extend(line1)
                lines[j] = line_new
            else: # not connected
                found_connected=False
                pass
            if found_connected:
                print('index=',index)
                print('line= ',line)
                print('line1=',line1)
                print(lines)
                del lines[index]

        
    
    
def main():
    xy_list = sample()
    print('xy_list=',xy_list)

    lines=[]
    line0=[xy_list[0]]
    lines.append(line0)
    for x,y in xy_list[1:]:    #go through each point
        found_in_line=False
        for line in lines:     #go through each line
            if in_the_line((x,y),line):
                print(f"{(x,y)} is in the line {line}. add into it")
                found_in_line = True
                pass
        if not found_in_line:
            # create a new line
            line1 = [(x,y)]
            lines.append(line1)
    print('found all lines:',lines)


    # now combine lines

    combine_lines(lines)

    print('combine:','\n'.join(str(_) for _ in lines))
main()


    

