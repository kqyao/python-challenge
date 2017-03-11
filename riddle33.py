from PIL import Image
import math

im=Image.open('beer2.png')
print(im.format, im.size, im.mode) #PNG (138, 138) L
#print(im.histogram())
#print(im.getcolors())
#print(len(im.getcolors())) #66
color=im.getcolors()
h=[]
#for i in range(len(im.histogram())):
#    if im.histogram()[i]!=0:
#        h=h+[im.histogram()[i]]
#print(h)
data=im.getdata()
data2=[]
dataNew=[]
for j in range(33):
    data2=[]
    dataNew=[]
    size=0
    for i in range(len(data)):
        if data[i] == color[65-2*j][1]: #most powerful
            data2=data2+[1]
        elif data[i] == color[64-2*j][1]:
            data2=data2+[0]
        else:
            dataNew=dataNew+[data[i]]
            data2=data2+[0]
        size=size+1
    #print(size)
    #print(data2)
    size=int(math.sqrt(size))
    imNew=Image.new('1', (size,size))
    imNew.putdata(data2)
    imNew.save('riddle33_answer%d.png'%(j+1))
    data=dataNew
    
