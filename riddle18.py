import gzip
import difflib

z1=gzip.open('deltas.gz','r')
file_content=z1.read()
file_content=file_content.splitlines()
left=[]
right=[]
for i in file_content:
    left=left+[i[0:53].decode()]
    right=right+[i[56:109].decode()]
    #print(i)
#print(len(file_content), len(left), len(right))
z1.close
diff = list(difflib.ndiff(left,right))
#print(diff)

f1 = open('riddle18_answer1.png', 'wb')
f2 = open('riddle18_answer2.png', 'wb')
f3 = open('riddle18_answer3.png', 'wb')
for i in diff:
    b = bytes([int(j, 16) for j in i[2:].split()])
    if i[0]=='-': f1.write(b) 
    elif i[0]=='+': f2.write(b)  
    elif i[0]==' ': f3.write(b) 
f1.close()
f2.close()
f3.close()
