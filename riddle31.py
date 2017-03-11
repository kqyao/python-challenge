#kohsamui:thailand
from PIL import Image

im=Image.open('mandelbrot.gif')
print(im.format, im.size, im.mode) #GIF (640, 480) P

left=0.34
top=0.57
width=0.036
height=0.027
it=128
im2=Image.new('P', (640,480))

List=[]
#radii=2
#for j in range(480):
for j in range(479, -1, -1):
    for i in range(640):
        c=complex(i*width/640+left, j*height/480+top)
        a=complex(0,0)
        for k in range(128):
            a=a**2+c
            if a.real**2+a.imag**2>4:
                break
        im2.putpixel((i,479-j),k)
        if k!=im.getpixel((i,479-j)):
            List=List+[k-im.getpixel((i,479-j))]
print(len(List))
#1679=23*73
im2.save('riddle31_pic.png')
im3=Image.new('1', (23,73))
List2=[]
for i in List:
    if i<0:
        List2=List2+[1]
    else:
        List2=List2+[0]
im3.putdata(List2)
im3.save('riddle31_answer.png')
#arecibo
