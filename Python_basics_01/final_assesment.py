
#  ✅❌


# # 1. defined 5 python data type and give an example each--->  ✅ 4.5/5
# 1. String - a collection of data in "", ''e.g ("name", "age")
# 2. Tuple - stores only unique numbers e.g (1,2,3)
# 3. Dictionary - a collection of data in {} and it holds a key and value pair e.g {"name":20}
# 4. Boolean - True or False or 0 or 1
# 5. list - a collection of data in [], e. g ["name", "age"] 


# 2. define module and package ✅ 5/5
# 1.A module is a python file
# 2.A package is a folder/directory that contains one or more files in python  

# 3. Define class and Instance ✅ 5/5
# 1. Class is a parent Code or template for creating instances
# 2. Instance is the child of a class
        
# 4. What are the 5 characteristics of a class ✅ 4.5/5
# 1. Inheritance
# 2. Polymorphism
# 3. Encapsulation
# 4. Abstraction
# 5. Modularity


# 35 + 12.5 = 47.5/50 --> A student
   

# 5. write a  class Human, ✅ 3.5/5
#     - with two General attributes soul and spirit both with value True
#     - with three instance attributes gender, age, nationality
#     - create 2 methods for this class on your own

# class Human:
#     soul = True
#     spirit = True

#     def __init__(self,gender, age, nationality):
#         self.gender = gender
#         self.age = age
#         self.nationality = nationality
        
#     def result1(self):
#         print(f"{self.soul} needs renewer of the mind.")
        
#     def result2(self):
#         print(f"{self.spirit} is clean and gentle as a dove.")    
  
# # instantiate class   
# w = Human("Female", 28, "Togolese")
# w.result1()
# w.result2()

       
# 6. Create an array with 5 elements. Write a forloop to print each out. ✅ 5/5
# colour = ["pink", "yellow", "orange", "white", "black"]

# for t in colour:
#     print(t)

# # # 7. Create an array with 6 elements. Write a while to print each out ✅ 5/5
# colour = ["pink", "yellow", "orange", "white", "black", "indigo"]
    
# f = 0
# while f < len(colour):
#     print(colour[f])
#     f += 1

    

# 8. write a function called "love". It should take two argument boy_name and girl_name. It should print dynamically
#    boy_name is in love with girl_name ✅ 5/5

# def love(boy_name, girl_name):
#     print(f"{boy_name} is in love with {girl_name}")
    
# love("sanni", "amidat")    

 

# 9. write a function called checker ✅ 5/5
#      It should ask for the user input from 0-5 ( put this in the placeholder)
#      control logic ( using if, elif and else).
#          if number is less than or eqal to 2, print "Beginner"
#          if number is greater than or eqal to 3 and less than or equal to 4, print "Intermediate"
#          if number is 5, print expert
      
       
# def checker():
#     user_input = int(input("Please enter your code (0-5):  "))
#     if user_input <= 2:
#         print("Beginner") 
#     elif user_input >= 3 and user_input <= 4:
#         print("Intermediate")  
#     else:
#         print("Expert")   
        
# checker()   
               
    

# 10. Write a function called 'python_experience'. ✅ 5/5
# It should take your name and return your python experience in the form below
# '{name} python experience is awesome'

def python_experience(name):
    return f"{name}'s experience is awesome."

# kk=python_experience("Shalom")
# print(kk)

print(python_experience("Shalom"))