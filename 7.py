#Creating objects (or variables of a class type): 

class CSStudent:
  
    # Class Variable
    stream = 'ECE'           
  
    # The init method or constructor
    def __init__(self, roll):
    
        # Instance Variable    
        self.roll = roll       
   
# Objects of CSStudent class
a = CSStudent(101)
b = CSStudent(102)
   
print(a.stream)  # prints "ECE"
print(b.stream)  # prints "ECE"
print(a.roll)    # prints 101
   
# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "ECE"  