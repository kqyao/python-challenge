import urllib.request
import bz2
s='http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html'
opener = urllib.request.FancyURLopener()
response = opener.open(s)
html = response.readlines()
#print(len(html))#84
#print(html[12])
b=b''
for i in range(12,84):
    b=b+''.join(chr(len(html[i])-1)).encode()
#print(b)
#b=b'BZh91AY&SY\xd9\xc2p\x18\x00\x00\x04\x9d\x80`\x80\x00\x00\x80 ./\x9c  \x001L\x98\x99\x06F\x112hd\x06jUd\xb9\x9e\xc6\x18\xc5\x92RH\xe5Z"\x01\xba\xa7\x80\x7f\x8b\xb9"\x9c(Hl\xe18\x0c\x00'

print(bz2.decompress(b))

#Isn't it clear? I am yankeedoodle!
