#Python program to check if lowercase letters exist in a string
'''s='Vani'
for i in s:
    k=i.islower
    if k==True:
        print('True')
        break
    if k!=1:
        print('False')'''

str = "Live life to the Fullest"
  
# Traversing Each character of 
# the string to check whether 
# it is in lowercase 
for char in str: 
    k = char.islower()   
    if k == True: 
        print('True') 
          
    # Break the Loop when you 
    # get any lowercase character. 
        break  
  
# Default condition if the string 
# does not have any lowercase character. 
if(k != 1): 
    print('False')         
        