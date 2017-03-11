import this
import string
table=str.maketrans(string.ascii_lowercase,string.ascii_lowercase[13:]+string.ascii_lowercase[:13])
s1='va gur snpr bs jung?'
s2=''
s2=str.translate(s1,table)
print(s2)

#in the face of what?
#In the face of ambiguity, refuse the temptation to guess.
