def printTable(A):
    print('   ', end='')
    for i in range(10):
        print(i, end='  ')
    for i in range(10, 32):
        print(i,end=' ')
    print('')
    for i in range(32):
        if i<10:
            print(i, end='  ')
        else:
            print(i, end=' ')
        for j in range(32):
            print(A[i][j], end='  ')
        print('')

def step1(A, H, V):
    #add '1'
    for i in range(32):
        if sum(H[i])+len(H[i])-1>16:
            left=32-sum(H[i])+len(H[i])-1
            for j in range(len(H[i])):
                if H[i][j]>left:
                    #print(32-sum(H[i][j:])-len(H[i][j:])+1, sum(H[i][0:j+1])+len(H[i][0:j+1])-2)
                    for k in range(32-sum(H[i][j:])-len(H[i][j:])+1, sum(H[i][0:j+1])+len(H[i][0:j+1])-2):
                        A[i][k]=1
    for i in range(32):
        if sum(V[i])+len(V[i])-1>16:
            left=32-sum(V[i])+len(V[i])-1
            for j in range(len(V[i])):
                if V[i][j]>left:
                    for k in range(32-sum(V[i][j:])-len(V[i][j:])+1, sum(V[i][0:j+1])+len(V[i][0:j+1])-2):
                        A[k][i]=1

def helper(a, l):
    #find all posibilities
    p=[]
    for i in range(l-sum(a)-len(a)+2):
        q=[]
        for j in range(i):
            q=q+['X']
        for j in range(a[0]):
            q=q+[1]
        if len(a)==1:
            for j in range(l-len(q)):
                q=q+['X']
            p=p+[q]
        else:
            q=q+['X']
            pp=helper(a[1:], l-len(q))
            for k in pp:
                p=p+[q[::]+k[::]]
    return p
            
def update(p, index, value):
    pp=[]
    for i in range(len(p)):
        if p[i][index]==value:
            pp=pp+[p[i]]
    return pp



A=[]
for i in range(32):
    A=A+[[]]
    for j in range(32):
        A[i]=A[i]+[0]
H=[[3,2],[8],[10],[3,1,1],[5,2,1],[5,2,1],[4,1,1],[15],[19],[6,14],
            [6,1,12],[6,1,10],[7,2,1,8],[6,1,1,2,1,1,1,1],[5,1,4,1],[5,4,1,4,1,1,1],
            [5,1,1,8],[5,2,1,8],[6,1,2,1,3],[6,3,2,1],[6,1,5],[1,6,3],[2,7,2],[3,3,10,4],
            [9,12,1],[22,1],[21,4],[1,17,1],[2,8,5,1],[2,2,4],[5,2,1,1],[5]]
V=[[5],[5],[5],[3,1],[3,1],[5],[5],[6],
          [5,6],[9,5],[11,5,1],[13,6,1],[14,6,1],[7,12,1],[6,1,11,1],[3,1,1,1,9,1],
          [3,4,10],[8,1,1,2,8,1],[10,1,1,1,7,1],[10,4,1,1,7,1],[3,2,5,2,1,2,6,2],[3,2,4,2,1,1,4,1],[2,6,3,1,1,1,1,1],[12,3,1,2,1,1,1],
          [3,2,7,3,1,2,1,2],[2,6,3,1,1,1,1],[12,3,1,5],[6,3,1],[6,4,1],[5,4],[4,1,1],[5]]

step1(A, H, V)
#step2(A, Horizontal, Vertical)
pH=[]
pV=[]

for i in range(32):
    pH=pH+[helper(H[i], 32)]
    #print(i)
    pV=pV+[helper(V[i], 32)]
    #print(i)
count=0
for i in range(32):
    for j in range(32):
        if A[i][j]==1:
            update(pH[i], j, 1)
            update(pV[j], i, 1)
            count=count+1
while count < 32*32:
    for i in range(32):
        if len(pH[i])==0:
            continue
        elif len(pH[i])==1:
            for j in range(32):
                if A[i][j]==0:
                    A[i][j]=pH[i][0][j]
                    pV[j]=update(pV[j], i, pH[i][0][j])
                    count=count+1
            pH[i].pop(0)
        else:
            for j in range(32):
                if A[i][j]==0:
                    for k in pH[i][1::]:
                        if k[j]!=pH[i][0][j]:
                            break
                    else:
                        A[i][j]=pH[i][0][j]
                        pV[j]=update(pV[j], i, pH[i][0][j])
                        count=count+1
    for i in range(32):
        if len(pV[i])==0:
            continue
        elif len(pV[i])==1:
            for j in range(32):
                if A[j][i]==0:
                    A[j][i]=pV[i][0][j]
                    pH[j]=update(pH[j], i, pV[i][0][j])
                    count=count+1
            pV[i].pop(0)
        else:
            for j in range(32):
                if A[j][i]==0:
                    for k in pV[i][1::]:
                        if k[j]!=pV[i][0][j]:
                            break
                    else:
                        A[j][i]=pV[i][0][j]
                        pH[j]=update(pH[j], i, pV[i][0][j])
                        count=count+1

#print(len(pH[0]))
#print(len(Horizontal))
printTable(A)
#Congrats! You made it through to the smiling python.

#"Free" as in "Free speech", not as in "free...

#beer
