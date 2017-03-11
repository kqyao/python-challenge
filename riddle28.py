from PIL import Image
#green.html

im=Image.open('bell.png')
r, g, b=im.split()

data=g.getdata()
#for i in range(10):
    #print(data[i])
#42
for i in range(0,len(data),2):
    if abs(data[i]-data[i+1])!=42:
        #print(i)
        print(chr(abs(data[i]-data[i+1])),end='')
print('')
im.close()

#whodunnit().split()[0] ?

#Who done it
#'Guido van Rossum'
