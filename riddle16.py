from PIL import Image

im=Image.open('mozart.gif')
print(im.format, im.size, im.mode) #size=(640, 480)
#for i in range(430,432):
#    print(im.getdata()[i]==195)

#pink = 195
imNew=Image.new('P',(640,480))
for y in range(480):
    for i in range(640):
        if im.getdata()[640*y+i]==195:
            if im.getdata()[640*y+i+1]==195 and im.getdata()[640*y+i+2]==195:
                x=i
    for i in range(640):
        if i+x>=640:
            x=x-640
        imNew.load()[i,y]=im.getdata()[640*y+i+x]
imNew.save('riddle16_answer.gif', 'GIF')

#romance
