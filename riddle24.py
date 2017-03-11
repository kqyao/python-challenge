from PIL import Image

im=Image.open('maze.png')
print(im.format, im.size, im.mode) #PNG (641, 641) RGBA
#for i in range(409599,410240):
#    print(im.getdata()[i])
#(0,0,0,255) is wall

graph=[]
parent=[]
for i in range(641):
    graph=graph+[[]]
    parent=parent+[[]]
    for j in range(641):
        parent[i]=parent[i]+[None]
        if im.getdata()[641*i+j]==(255,255,255,255):
            graph[i]=graph[i]+[0] #wall
        else:
            graph[i]=graph[i]+[1] #road
#imNew=Image.new('RGBA',(641,641),(0,0,0))
#for i in range(641):
#    for j in range(641):
#        if graph[i][j]==1:
#            imNew.load()[i,j]=(255,255,255,255)
#imNew.save('riddle24_graph.jpg','JPEG')
y=0
x=639
parent[y][x]=0
#DFS
stack=[[x,y]]
while(len(stack)!=0):
    [x,y]=stack[0]
    if [x,y]==[1,640]:
        break
    stack.pop(0)
    if y<640:
        if graph[y+1][x]==1 and parent[y+1][x]==None:
            parent[y+1][x]=[x,y]
            stack=[[x,y+1]]+stack
    if x>0:
        if graph[y][x-1]==1 and parent[y][x-1]==None:
            parent[y][x-1]=[x,y]
            stack=[[x-1,y]]+stack
    if x<640:
        if graph[y][x+1]==1 and parent[y][x+1]==None:
            parent[y][x+1]=[x,y]
            stack=[[x+1,y]]+stack
    if y>0:
        if graph[y-1][x]==1 and parent[y-1][x]==None:
            parent[y-1][x]=[x,y]
            stack=[[x,y-1]]+stack
#print('over')
#print(parent[640][1])
#print(parent[5][639])
            
imNew=Image.new('RGBA',(641,641),(0,0,0))
path=[[1,640]]
p=parent[640][1]
while(p!=0):
    [x,y]=p
    path=[p]+path
    p=parent[y][x]
    imNew.load()[x,y]=(255,255,255,255)
imNew.save('riddle24_graph2.jpg','JPEG')
solution=open('riddle24_solution.zip','wb')
strings=''
byte=[]
for i in path:
    [x,y]=i
    byte.append(im.getpixel((x,y))[0])
    strings=strings+str(im.getdata()[641*x+y][0])
for i in byte[1::2]:
    solution.write(chr(i))
#print(bytes(byte))
    #print(strings)
#solution.write(bytes(strings,encoding='utf-8'))
solution.close()
#linux
