s1='g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr''q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
s2=''
for i in list(range(len(s1))):
    if ord(s1[i])>96 and ord(s1[i])<121:
        s2=s2+chr(ord(s1[i])+2)
    else:
        if ord(s1[i])==121:
            s2=s2+'a'
        else:
            if ord(s1[i])==122:
                s2=s2+'b'
            else:
                s2=s2+s1[i]
print(s2)

s1='map'
s2=''
for i in list(range(len(s1))):
    if ord(s1[i])>96 and ord(s1[i])<121:
        s2=s2+chr(ord(s1[i])+2)
    else:
        if ord(s1[i])==121:
            s2=s2+'a'
        else:
            if ord(s1[i])==122:
                s2=s2+'b'
            else:
                s2=s2+s1[i]
print(s2)
