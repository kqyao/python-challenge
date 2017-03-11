import wave
from PIL import Image

images=[]
for i in range(1,26,1):
    f1=wave.open('lake%d.wav'%i,'rb')
    #print(f1.getnframes())#10800
    #waves=[]
    #for i in list(range(f1.getnframes())):
    #waves=waves+[f1.readframes(1)]
    #im=Image.new('RGB',(60,60))
    image=Image.frombytes('RGB',(60,60), f1.readframes(10800))
    images=images+[image]
    #image=Image.frombytes('RGB',(60,60),f1.readframes(10800))
    #image.save('riddle25_pic%d.jpg'%i,'JPEG')
im=Image.new('RGB',(300,300))
for k in range(25):
    for j in range(60):
        for i in range(60):
            im.load()[(k%5)*60+i,(k//5)*60+j]=images[k].getdata()[60*j+i]
im.save('riddle25_solution.jpg','JPEG')

#decent
