import zipfile
z1=zipfile.ZipFile('channel.zip','r')
#print(z1.getinfo('90052.txt').comment)
fileName='90052.txt'
sout=''
for i in list(range(1000)):
    if fileName!='.txt':
        sout=sout+chr(z1.getinfo(fileName).comment[0])
        file1=z1.open(fileName,'r')
        text1=file1.read()
        fileName=''
        for j in range(len(text1)):
            if text1[j]>=ord('0') and text1[j]<=ord('9'):
                fileName=fileName+chr(text1[j])
        fileName=fileName+'.txt'
        #print(i)
        #print(text1)
        #print(fileName)
z1.close
print(sout)

#Collect the comments.

