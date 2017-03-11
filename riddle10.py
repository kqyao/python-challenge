a='1'
for i in range(30):
    k=1
    b=''
    for j in range(1,len(a)):
        if a[j]==a[j-1]:
            k=k+1
        else:
            b=b+str(k)
            b=b+str(a[j-1])
            k=1
    b=b+str(k)
    b=b+str(a[len(a)-1])
    a=b
    print(len(a))
        
#5808
