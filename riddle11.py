from PIL import Image

im=Image.open('cave.jpg')
print(im.format, im.size, im.mode) 
imNew=Image.new('RGBA',(im.size[0]//2,im.size[1]//2),(0,255,0))
for i in range(im.size[1]):
    for j in range(im.size[0]):
        if i//2==i/2 and j//2==j/2:
            imNew.load()[j//2,i//2]=im.getdata()[i*im.size[0]+j]
imNew.save('cave2.jpg','JPEG')

#evil
