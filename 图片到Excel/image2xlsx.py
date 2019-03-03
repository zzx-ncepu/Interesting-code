import sys
from PIL import Image 
import xlsxwriter as excel

def pixel2color(pix):
    th = 1 #scale color to enforce pixel effect
    r, g, b= int(pix[0]/th)*th, int(pix[1]/th)*th, int(pix[2]/th)*th
    return '#%02x%02x%02x'%(r, g, b)

def write_image_to_excel(fimage, fexcel):
    #对图片进行预处理
    img = Image.open(fimage).convert('RGB')
    img_width, img_height = img.size[0], img.size[1]
    if img_width>1048576 or img_height>16384: #限制一下表格的大小
        raise Exception("too large image")

    #创建一个excel表格
    wb = excel.Workbook(fexcel)
    ws = wb.add_worksheet('image')

    #
    pixel = img.load()	#方法load()返回一个用于读取和修改像素的像素访问对象
    for r in range(0, img_height):
        for c in range(0, img_width):
            # print 'dealing', r, c, pixel[c, r]
            fmt = wb.add_format({'pattern':1, 'bg_color': pixel2color(pixel[c,r])})
            ws.write(r, c, None, fmt)

    #修改一下每一小格的尺寸
    col_width = 1
    row_height = col_width * 10  #10佛系调出来的
    for r in range(0, img_height):
        ws.set_row(r, row_height)
    ws.set_column(0, img_width, col_width)

    print ('saving...', fexcel)
    wb.close() #this may cost lots of time

def main():
	#这句的意思是执行程序时候，需要两个参数，（在命令行）例如：python image2xlsx.py ***.jpg
	#注意的是image2xlsx.py也是一个参数
	#所以只用加上照片路径即可
    if len(sys.argv)==2: 
        write_image_to_excel(sys.argv[1], sys.argv[1]+'.xlsx')
    else:
        print('usage: python image2xlsx.py image.png')

if __name__ == '__main__':
    main()



