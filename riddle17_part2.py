import bz2
import http.cookiejar
import urllib.request

b=b'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$\x90'
print(bz2.decompress(b))

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

print(s.system.listMethods())
print(s.system.methodHelp('phone'))

#print(s.phone('evil'))

#http://www.pythonchallenge.com/pc/return/evil4.jpg

#print(s.phone('Bert'))
print(s.phone('Leopold'))
#violin
#http://www.pythonchallenge.com/pc/stuff/violin.php
request=urllib.request.Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
request.add_header('Cookie','info=the flowers are on their way')
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
print(response.read())
#balloons
