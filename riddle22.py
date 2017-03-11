from PIL import Image
from PIL import ImageSequence

im=Image.open('white.gif')
print(im.format, im.size, im.mode) #GIF (200, 200) P
it=ImageSequence.Iterator(im)
print(len(list(it)))#133
for i in range(133):
    im2=it[i]
    for j in range(40000):
        if im2.getdata()[j]!=0:
            if j==20100:
                print(i,j)

imNew=Image.new('P', (200,200))
for i in range (0,200):
    for j in range (200):
        imNew.load()[i,j]=100
x=100
y=100
for i in range(29):
    im2=it[i]
    for j in range(40000):
        if im2.getdata()[j]!=0:
            if j%100==98:
                x=x-1
            if j%100==2:
                x=x+1
            if j>20400:
                y=y+1
            if j<19800:
                y=y-1
            imNew.load()[x,y]=0
imNew.save('riddle22_answer1.gif','GIF')

imNew=Image.new('P', (200,200))
for i in range (200):
    for j in range (200):
        imNew.load()[i,j]=100
x=100
y=100
for i in range(29,55):
    im2=it[i]
    for j in range(40000):
        if im2.getdata()[j]!=0:
            if j%100==98:
                x=x-1
            if j%100==2:
                x=x+1
            if j>20400:
                y=y+1
            if j<19800:
                y=y-1
            imNew.load()[x,y]=0
imNew.save('riddle22_answer2.gif','GIF')

imNew=Image.new('P', (200,200))
for i in range (200):
    for j in range (200):
        imNew.load()[i,j]=100
x=100
y=100
for i in range(55,80):
    im2=it[i]
    for j in range(40000):
        if im2.getdata()[j]!=0:
            if j%100==98:
                x=x-1
            if j%100==2:
                x=x+1
            if j>20400:
                y=y+1
            if j<19800:
                y=y-1
            imNew.load()[x,y]=0
imNew.save('riddle22_answer3.gif','GIF')

imNew=Image.new('P', (200,200))
for i in range (200):
    for j in range (200):
        imNew.load()[i,j]=100
x=100
y=100
for i in range(80,101):
    im2=it[i]
    for j in range(40000):
        if im2.getdata()[j]!=0:
            if j%100==98:
                x=x-1
            if j%100==2:
                x=x+1
            if j>20400:
                y=y+1
            if j<19800:
                y=y-1
            imNew.load()[x,y]=0
imNew.save('riddle22_answer4.gif','GIF')

imNew=Image.new('P', (200,200))
for i in range (200):
    for j in range (200):
        imNew.load()[i,j]=100
x=100
y=100
for i in range(101,133):
    im2=it[i]
    for j in range(40000):
        if im2.getdata()[j]!=0:
            if j%100==98:
                x=x-1
            if j%100==2:
                x=x+1
            if j>20400:
                y=y+1
            if j<19800:
                y=y-1
            imNew.load()[x,y]=0
imNew.save('riddle22_answer5.gif','GIF')
im.close()
