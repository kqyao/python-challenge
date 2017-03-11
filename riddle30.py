from PIL import Image
import re

#53*139

f=open('yankeedoodle.csv','r')
content=f.read()
#print(content[:100])

data = re.findall('0.\d+',content) 
#print(data[:10])
#print(len(data))
#im=Image.new('F',(53,139))
#im.putdata(data)

dataS=b''
for i in data:
    dataS=dataS+chr(int((float(i)*256)//1))
#print(dataS[:10])
im=Image.frombytes('L', (53,139), dataS)
im=im.transpose(Image.ROTATE_90)
im=im.transpose(Image.FLIP_LEFT_RIGHT)
im.show()

#n=str(x[i])[5]+str(x[i+1])[5]+str(x[i+2])[6]

for i in range(0,len(data)-3,3):
    print(chr(int(str(data[i])[5]+str(data[i+1])[5]+str(data[i+2])[6])))

#So, you found the hidden message.
#There is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage. 
