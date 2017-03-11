import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

print(s.system.listMethods())
print(s.system.methodHelp('phone'))

print(s.phone('evil'))

#http://www.pythonchallenge.com/pc/return/evil4.jpg

print(s.phone('Bert'))
