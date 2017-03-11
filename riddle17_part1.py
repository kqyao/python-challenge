import http.cookiejar
import urllib.request
import urllib.parse
import bz2

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php')
for item in cookie:
    print('Name = ', item.name)
    print('Value = ', item.value)
#Cookie Reference: http://python.jobbole.com/81344/
c=''
s='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345'
response = urllib.request.urlopen(s)
r=opener.open(s)
for item in cookie:
    c=c+item.value

s='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=44827'
#print(len(s))
for i in list(range(117)):
    response = urllib.request.urlopen(s)
    r=opener.open(s)
    html = response.read()
    html2=html
    s1=s[0:65]
    for j in list(range(len(html))):
        if html[j]>=48 and html[j]<=57:
            s1=s1+chr(html[j])
    s=s1
    #j=i
    #print(j)
    #print(html2)
    #print(s1)
    for item in cookie:
        if item.name=='info':
            c=c+item.value
        #print(c)
print(c)
b=urllib.parse.unquote_plus(c)
print(b)
#BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$\x90
#solved in part2
