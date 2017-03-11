import urllib.request
import re  
url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'
opener = urllib.request.FancyURLopener()
f=opener.open(url)
print(f.info())
#start=30203
#start=2123456788
#esrever ni emankcin wen ruoy si drowssap eht
#the password is your new nickname in reverse
start=2123456743
#b'and it is hiding at 1152983631.\n'
start=1152983631
end=2123456789
regex=re.compile('bytes \d*-(\d*)')
print(re.findall(regex,str(f.info())))
#for i in range(5):
for i in range(1):
    opener.addheader('Range','bytes=%d-%d' % (start,end))
    f=opener.open(url)
    print(f.info())
    fi=re.findall(regex,str(f.info()))
    #print(fi)
    start=int(fi[0])+1
    #print(f.read())
    open('riddle20_answer.zip','wb').write(f.read())
