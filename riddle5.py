import pickle
import urllib.request
u='http://www.pythonchallenge.com/pc/def/banner.p'
response=urllib.request.urlopen(u)
html=response.read()
t=pickle.loads(html)
for i in list(range(len(t))):
    string1=""
    for j in list(range(len(t[i]))):
        for k in list(range(t[i][j][1])):
            string1=string1+t[i][j][0]
    print(string1)
