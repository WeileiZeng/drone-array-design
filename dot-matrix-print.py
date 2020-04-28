
import binascii
import random
# define constants
KEYS = [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]
# size=16 # size of the dot matrix, 16 or 32
# font_filename='HZK16';

blue='\033[36m'
red='\033[31m'
dark='\033[30m'
light_white='\033[29m'
green='\033[32m'
grey='\033[90m'


    
def get_offset(character):
    # return the offset of that character in GB2312
    text=character
    if (len(character) != 1):
        raise ValueError("character lenght not equals 1")
        
    if ( ord(text)< 128) :
        # utf-8 characters can not be determined by the dedault method, so take care of them here
        area=3
        #area = eval('0xA3') - 0xA0 # output 3
        
        index=ord(text)-32  # it is 32 but not sure why. It comes from the difference between ord() and gb2312
        offset = (94 * (area-1) + (index-1)) * 32
#        print('it is an english word: ',text, 'with ord ',ord(text),'area',area)
        return offset

    #other wise it is a chainese character        
    gb2312 = text.encode('gb2312')
    #将二进制编码数据转化为十六进制数据
    hex_str = binascii.b2a_hex(gb2312)
    #将数据按unicode转化为字符串
    result = str(hex_str, encoding='utf-8')

    #前两位对应汉字的第一个字节：区码，每一区记录94个字符
    area = eval('0x' + result[:2]) - 0xA0
    #后两位对应汉字的第二个字节：位码，是汉字在其区的位置
    index = eval('0x' + result[2:]) - 0xA0
    #汉字在HZK16中的绝对偏移位置，最后乘32是因为字库中的每个汉字字模都需要32字节
    offset = (94 * (area-1) + (index-1)) * 32
    return offset

def get_dot_matrix(offset,font_file_name='HZK16', size=16):
    # get the dot_matrix according to the offset. offset is the position of the character in GB2312
    font_rect = None

    #读取HZK16汉字库文件
    with open("HZK16", "rb") as f:
        #找到目标汉字的偏移位置
        f.seek(offset)
        #从该字模数据中读取32字节数据. 32 for size=16, 128 for size=32
        font_rect = f.read(32)
    rect_list=[]
    
    #font_rect的长度是32，此处相当于for k in range(16)
    for k in range(len(font_rect) // 2):
        #每行数据
        row_list = []
        for j in range(2):
            for i in range(8):
                asc = font_rect[k * 2 + j]
                #此处&为Python中的按位与运算符
                flag = asc & KEYS[i]
                #数据规则获取字模中数据添加到16行每行中16个位置处每个位置
                row_list.append(flag)
        rect_list.append(row_list)
    return rect_list


def print_dot_matrix(dot_matrix, symbol='O', background='.',color=green):
    # print the dot_matrix to stdout
    # dot_matrix is just a 2D list with some nonzero or zero elements

    symbol=color+symbol
    background = grey+background
    for row in dot_matrix:
        for i in row:
            if i :
                print(symbol,end=' ')
            else:
                print(background, end=' ')
        print()
        
def print_character(character, color = green):
    # print the dot matrix of a single character
    text=character
    offset = get_offset(text)
    dot_matrix = get_dot_matrix(offset, color = color)
    print_dot_matrix(dot_matrix)

def merge_dot_matrix_horizontally(m1,m2):
    # to print multiple characters in one line, just merge their dot matrix and then print
    for i in range(0,len(m1)):
        m1[i] = m1[i] +m2[i]
    return m1

def get_random_color():
    n=random.randint(25,38)
    return '\033['+str(n)+'m'

        
def print_sentence(sentence, width=1):
    if ( width == 1 ):
        for character in sentence:
            print_character(character)
    else:
        i=0
        dot_matrix=None
        for character in sentence:
            i+=1
            if (i ==1):
                dot_matrix = get_dot_matrix(get_offset(character))
            else:
                dot_matrix = merge_dot_matrix_horizontally( dot_matrix, get_dot_matrix(get_offset(character)) )
                if ( i == width ):
                    print_dot_matrix(dot_matrix, color = get_random_color())
                    i=0
        if ( i < width and i > 0  ):
            print_dot_matrix(dot_matrix)                
            
                
def test(text):
    offset = get_offset(text)
#    offset = get_offset('啊')
    dot_matrix = get_dot_matrix(offset)
    symbol='O'
    symbol='\033[91mO\033[90m'
    background='.'
    print_dot_matrix(dot_matrix, symbol, background )

    
if __name__ == "__main__":
    print_sentence('你好，world', width = 4)
#    for text in 'abcdefABCDEF,.:/;':
#            test(text)
