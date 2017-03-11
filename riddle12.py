f = open('evil2.gfx', 'rb')
data = f.read()
f.close()

f=open('riddle12_1.jpg', 'wb')
f.write(data[0::5])
f.close()

f=open('riddle12_2.jpg', 'wb')
f.write(data[1::5])
f.close()

f=open('riddle12_3.jpg', 'wb')
f.write(data[2::5])
f.close()

f=open('riddle12_4.jpg', 'wb')
f.write(data[3::5])
f.close()

f=open('riddle12_5.jpg', 'wb')
f.write(data[4::5])
f.close()
