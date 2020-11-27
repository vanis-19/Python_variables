test_str = 'one two three four'
s=test_str.split()
l=[]
for i in range(len(s)):
    if i%2==0:
        l.append(s[i][::-1])
    else:
        l.append(s[i])
print(' '.join(l))            