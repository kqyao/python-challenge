import urllib.request
s='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

#print(len(s))
for i in list(range(400)):
    response = urllib.request.urlopen(s)
    html = response.read()
    html2=html
    s1=s[0:61]
    for j in list(range(len(html))):
        if html[j]>=48 and html[j]<=57:
            s1=s1+chr(html[j])
    s=s1
    j=i
    print(j)
    print(html2)
    print(s1)
