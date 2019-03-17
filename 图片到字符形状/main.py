from PIL import Image
#import argparse
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r +0.7152*g +0.0722*b)

    uint = (256.0+1)/length
    return ascii_char[int(gray/uint)]

if __name__ == '__main__':
    
    img = Image.open('c:/Users/15412/Desktop/python/1/wm.png')
    im = img.convert('RGB')
    #img = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    img = img.resize((80,80),Image.NEAREST)  #nearest低质量 

    txt = ''

    for i in range(80):
        for j in range(80):
            txt += get_char(*img.getpixel((j,i)))
        txt += '\n'
    
    print(txt)
    with open('output.txt','w') as f:
        f.write(txt)