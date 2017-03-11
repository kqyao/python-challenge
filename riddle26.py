#Never mind that.

#Have you found my broken zip?

#md5: bbb8b499a0eef99b52c7f13f4e78c24b

#Can you believe what one mistake can lead to?



from hashlib import md5

real='bbb8b499a0eef99b52c7f13f4e78c24b'
broken=open('mybroken.zip','rb')
content=broken.read()

for i in range(256):
    for j in range(len(content)):
        if md5(content[0:j]+chr(i)+content[(j+1):]).hexdigest() ==real:
            open('riddle26_answer.zip','wb').write(content[0:j]+chr(i)+content[(j+1):])
            break
broken.close()

#linux
