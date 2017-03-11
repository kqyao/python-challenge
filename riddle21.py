import zlib
import bz2
f1=open('package.pack','rb')
content=f1.read()
flag=0
while 1:
    try:
        content=zlib.decompress(content)
        flag=0
        print(' ', end='')
    except:
        try:
            content=bz2.decompress(content)
            flag=0
            print('1', end='')
        except:
            content=content[::-1]
            flag=flag+1
            print('')
            if flag==3:
                break
f1.close()
#print(content)
#b'look at your logs'

#copper
