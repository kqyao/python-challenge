from PIL import Image

im=Image.open('index.png')
print(im.format, im.size, im.mode) #size=(10000, 1)
imNew=Image.new('RGBA',(100,100),(0,255,0))
visit=[]
for i in range(100):
    visit=visit+[[]]
    for j in range(100):
        visit[i]=visit[i]+[0]
x=-1
y=0
d=0
for i in range(10000):
    if d==0:
        if x==99:
            d=1
        else:
            if visit[x+1][y]==1:
                d=1
    if d==1:
        if y==99:
            d=2
        else:
            if visit[x][y+1]==1:
                d=2
    if d==2:
        if x==0:
            d=3
        else:
            if visit[x-1][y]==1:
                d=3
    if d==3:
        if y==0:
            d=0
        else:
            if visit[x][y-1]==1:
                d=0
    if d==0:
        x=x+1
    if d==1:
        y=y+1
    if d==2:
        x=x-1
    if d==3:
        y=y-1
    #print(x,y)
    imNew.load()[x,y]=im.getdata()[i]
    visit[x][y]=1
imNew.save('riddle14_answer.jpg','JPEG')

#cat
#uzi
