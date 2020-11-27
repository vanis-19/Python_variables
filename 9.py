#Python Program that Displays Letters that are not common in two strings
s1='india'
s2='austraila'
a=list(set(s1)^set(s2))
for i in a:
    print(i)
#l1=set(s1)
#l2=set(s2)
#output=l1^l2
#print(' '.join(output))