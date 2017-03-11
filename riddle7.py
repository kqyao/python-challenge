from PIL import Image

im=Image.open('oxygen.png')
print(im.format, im.size, im.mode) #size=(625,95)
for i in range(45*625,47*625,7):
    print(chr(im.getdata()[i][0]),end='')

#[105, 110, 116, 101, 103, 114, 105, 116, 121]

l=[105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in l:
    print(chr(i),end='')
