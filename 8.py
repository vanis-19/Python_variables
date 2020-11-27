#Python program to calculate the number of digits and letters in a string

s="python1234"
digits=0
alpha=0
for i in s:
    if i.isnumeric():
        digits=digits+1
    else:
        alpha=alpha+1
print("Total letters found :-", digits) 
print("Total digits found :-", alpha)         
