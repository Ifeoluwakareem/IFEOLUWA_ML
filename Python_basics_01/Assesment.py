# Define 5 python data type and give an example each:
#     1. string e.g "", '', '  ','quert'
#     2. list - this is a collection of data within [] e.g [], ["a,", "b", "c"], [1, 2, 3]
#     3. dictionary - this is a collection of data within {} stored as key:value pair e.g
#     {'ola':1, 2:'bimbo', 4:9, 1:[], 'v':{} }
#     4. tuple --> similar to list but stores only unique elements e.g  (1,2,3), (4, 5, 7), ("gender", "age", "nationality")
#     5. Boolean --> this holds boolean values e.g True, False
#     6. Interger
#     7. float

# Define module and package    
     # A package is a directory/folder that contains one or more files/modules
     # A module is a file
    
# Define class and Instance
    # class is defined as a parent code/object  
    # Instance is defined as the child of a class
    
# What are the 5 characteristics of a class 
   # solution: The characteristics of a class 
   # 1. Abstraction --> Hididing complex details
   # 2. Encapsulation --> grouping attributes and methods together
   # 3. Modularity    --> Each class code is self sufficient or stand complete
   # 4. Inheritance   --> A class can inherit from another one
   # 5. Polymorphism  --> different class with same name of attributes and methods but returns different output 
   
# What are the components of a class
        
  # 1. Attribute ( general attributes and Insatnce attribute)
  # 2. Methods 
  
# write a  class Human, 
#   - with two General attributes soul and spirit both with value True
#   - with three instance attributes gender, age, nationality
#   - create 2 methods for this class on your own 


# class Human:
#     # general attribute
#     soul = True
#     spirit = True 
    
#     # Instance attribute
#     def __init__(self, gender, age, nationality):
#         self.gender = gender
#         self.age = age
#         self.nationality = nationality
     
#     def shaman1(self): 
#         print(f"{self.soul} is possesed.")
        
#     def shaman2(self):
#         print(f"{self.spirit} is clean and gentle as a dove.")  

# # instantiate class                  
# k = Human("Male", 30, "Nigerian")  

# # call methods
# k.shaman1()
# k.shaman2()

# # general attribute
# print(k.soul, k.spirit)

# # Instance attributes
# print(k.gender, k.age, k.nationality)

# Create an array with 5 elements. Write a forloop to print each out ✅
# food = ["rice", "beans", "bread", "maize", "yam"]

# for r in food:
#     print(r) 

# Create an array with 6 elements. Write a while to print each out
# food = ["rice", "beans", "bread", "maize", "yam", "spag"]
       
# b = 0
# while b < len(food):
#     print(food[b])
#     b += 1   

# Write a function called "love". It should take two argument boy_name and girl_name. It should print dynamically
#    boy_name is in love with girl_name
# def love(boy_name, girl_name):
#     ff = f"{boy_name} is in love with {girl_name}."
#     print(ff)
    
# # love("kareem" , "shalom") 

# write a function called checker
          #  It should ask for the user input from 0-5 ( put this in the placeholder)
          #  control logic ( using if, elif and else).
          #  if number is less than or eqal to 2, print "Beginner"
          #  if number is greater than or eqal to 3 and less than or equal to 4, print "Intermediate"
          #  if number is 5, print expert 
          
def checker():
        user_input = int(input("Please enter your code (0-5):  "))
        
        if user_input <= 2:
                print("Beginner")
        elif user_input >= 3 and user_input <= 4:
                print("Intermediate")
        else:
                print("Expert")
                
# checker()   

# 10. Write a function called 'python_experience'.
# It should take your name and return your python experience in the form below
# '{name} python experience is awesome'

# def python_experience(name):
#      return(f"{name}'s python experience is awesome")  
        
        
# python_experience("Shalom")      
      
    




 