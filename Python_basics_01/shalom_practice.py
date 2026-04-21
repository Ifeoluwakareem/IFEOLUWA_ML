# family = ["father", "mother", "brother", "sister",  "uncle", "aunt", "nephew", "niece"]
# for n in family:
#     print(n)

# food = ["rice", "beans", "yam", "sausage"]
# for j in food:
#     print(j)
    
# w = 0
# while w < len(food):
#     print(food[w]) 
#     w += 1
    
# colour = ["pink", "blue", "yellow", "indigo"]
# for i in colour:
#     print(i)
    
# j = 0
# while j < len(colour):
#     print(f"running while loop when j is {j}")
#     print(colour[j])
#     j += 1    

# hardcode, hardcoding
# string literal

# print("my name is olawale 1")

# name="olawale"
# print(f"my name is {name}")

# biodata = {
#     "name": "ifeoluwa",
#     "age": "20",
#     "nationality": "nigeria"
    
#     }

# print(f"my biodata is  {biodata}")


# create a function that returns differnt user error based on the input of 1-3

# def user_response():
#     user_input = int(input("Please enter your code (1-3):  "))
#     if user_input not in [1, 2, 3]:
#         print('wrong user code entered')
#     if user_input == 1:
#         print("Access granted !!!")
#     if user_input == 2:
#         print("Revoked license !!!")
#     if user_input == 3:
#         print("Try again tommorow")
        
      
# user_response()

 
 
# def my_name(name):
#     print(f"my name is  {name}")
    
# my_name("olawale")    

# def my_name(name):
#     print(f"my name is  {name}")
    
# my_name("shalom")  

def gender_identity(identify):
    # identify = input("Please identify yourself: ")
    print(f"Your identity is  {identify}") 
     
    
# genders_array = ["Gay", "Straight", "Female"]

# for i in genders_array:
#     print(f"I am working on {i}")
#     gender_identity(i)
    

# k = 0
# while k < len(genders_array):
#     print(f"I am working on {genders_array[k]}")
#     gender_identity(genders_array[k])
    # k += 1
    
# genders_array = ["Gay", "Straight", "Female"]

# for i in genders_array:
#     print(f"I am working on {i}")
#     gender_identity(i)
    
# j = 0
# while j < len(genders_array):
#    print(f"I am working on {genders_array[j]}")  
#    gender_identity(genders_array[j])  
#    j += 1
    
# family = ["Father", "Mother", "Sister", "Uncle", "Aunt", "Nephew", "Niece"]
# for n in family:
#     print(n)
    
# j = 0
# while j < len(family):
#     print(family[j])
#     j += 1
    
    
  
# class FullName: #create a class called FullName
     
#      def __init__(self, name, dog): #special objects that runs when yoy create an object, takes in name and dog
#          self.name = name #saves the name inside the object
#          self.dog = dog #saves the dog's name inside the object
         
#      def namet(self): #defines a method (function inside class)
#          ret_name = f"My name is {self.name}" #create a sentence using the name
#          print(ret_name) #display the sentence
#          return ret_name #send the sentence back when the method is called
     
#      def name_dog(self): #defines a method 
#          ret_name = f"My name is {self.name} and my dog's name is {self.dog}" #create a sentence with name and dog
#          print(ret_name) #display it
#          return ret_name #return it


# FullNameInstance = FullName("Mork", "Pecky")  #create an object from the class Mork as name, Pecky as dog  
# my_name = FullNameInstance.namet() #call the first method, save the result in my_name
# my_name_dog = FullNameInstance.name_dog() #call the second method, save the result in my_name_dog

# name_name = FullNameInstance.name #get the name directly from the object
# print(name_name) #print the name

# dog_name = FullNameInstance.dog #get the dog's name
# print(dog_name) #print the dog's name    




# 1. defined 5 python data type and give an example each

        # a. String :a type of data that carries auguments in parentheses e.g "I am a girl" --> anything in between '' or "" ✅
        # b. Literals : integers(numbers), float(0.5), boolean(True or False)  ❌ --> Examples are correct but shouldn't be under literals
        # c. Variable : Red = gg , where red is the  variable ❌
        # d. Comments : # is used to make codes more explanatory and understandable ❌
                        #   Comments are not data types
        # e. Comparision : if, else, elif    ❌
                        # This is not a data type nor comparism
                        # if, else, elif --> used as flow control in python
        
        
        # solution
        # 1. String e.g "", '', '  ', 'qwert'
        # 2. list -->  This is a collection of data within [] e.g  [], ["a","b", "c"], [1,2,3]
        # 3. dictionary --> This is a collection of data within {} stored as key:value pair e.g {},
        #                               {'ola':1, 2:'bimbo', 4:9, 1:[], 'v':{} }
        # 4. tuple --> similar to list but stores only unique elements e.g  (1,2,3), (4, 5, 7), ("gender", "age", "nationality")
        # 5. Boolean --> this holds boolean values e.g True, False
        # 6. Interger
        # 7. float



# 2. define module and package 
        # package can be defined as a single file in python  ❌
                # A package is a directory/folder that contains one or more files/modules
        # module can be defined as multiple files also known as directory ❌
                # A module is a file

# 3. Define class and Instance
        # class is defined as a parent code/object  ✅
        # Instance is defined as the chilld (Child you mean) of a class. ✅
        
# 4. What are the 5 characteristics of a class
        # 1. Attribute ❌
        # 2. Method ❌
        # 3. Instance ❌
        # 4. __init__(self) ❌
        # 
        
        # solution: The characteristics of a class 
        # 1. Abstraction --> Hididing complex details
        # 2. Encapsulation --> grouping attributes and methods together
        # 3. Modularity    --> Each class code is self sufficient or stand complete
        # 4. Inheritance   --> A class can inherit from another one
        # 5. Polymorphism  --> different class with same name of attributes and methods but returns different output
        
        
        
        #Extra:  What are the components of a class
        
        # 1. Attribute ( general attributes and Insatnce attribute)
        # 2. Methods

# 5. write a  class Human, 
#     - with two General attributes soul and spirit both with value True
#     - with three instance attributes gender, age, nationality
#     - create 2 methods for this class on your own
#  

class Human:
        
#     ❌, general attribute is not defined at all       
        
#     ❌, instance attribute abstraction is wrong    
    def __init__(self, soul:True, spirit:True):
        self.soul = soul
        self.spirit = spirit
        
#     ✅    
    def shaman1(self): 
        print(f"{self.soul} is possesed.")
        
#     ✅    
    def shaman2(self):
        print(f"{self.spirit} is clean and gentle as a dove.")                     
K = ("gender", "age", "nationality")  # ❌, Class is never instanstiated,
#instead a variable k was give the value of  ("gender", "age", "nationality") tuple


## solutuion


class Human:
    # general attribute
    soul = True
    spirit = True 
    
    # Instance attribute
    def __init__(self, gender, age, nationality):
        self.gender = gender
        self.age = age
        self.nationality = nationality
        
#     ✅    
    def shaman1(self): 
        print(f"{self.soul} is possesed.")
        
#     ✅    
    def shaman2(self):
        print(f"{self.spirit} is clean and gentle as a dove.")  

# instantiate class                  
k = Human("Male", 30, "Nigerian")  

# call methods
k.shaman1()
k.shaman2()

# general attribute
print(k.soul, k.spirit)

# Instance attributes
print(k.gender, k.age, k.nationality )





       
# 6. Create an array with 5 elements. Write a forloop to print each out ✅
# food = ["rice", "beans", "bread", "maize", "yam"]

# for r in food:
#     print(r)

# # 7. Create an array with 6 elements. Write a while to print each out
# food = ["rice", "beans", "bread", "maize", "yam"]   # ❌ 6 elements not 5
    
# ✅    
# b = 0
# while b < len(food):
#     print(food[b])
#     b += 1    

# 8. write a function called "love". It should take two argument boy_name and girl_name. It should print dynamically
#    boy_name is in love with girl_name
# ✅
def love(boy_name, girl_name):
    ff = f"{boy_name} is in love with {girl_name}."
    print(ff)
    
# love("kareem" , "shalom")    

# 9. write a function called checker
    #  It should ask for the user input from 0-5 ( put this in the placeholder)
    #  control logic ( using if, elif and else).
        #  if number is less than or eqal to 2, print "Beginner"
        #  if number is greater than or eqal to 3 and less than or equal to 4, print "Intermediate"
        #  if number is 5, print expert
        
# def checker():       
#         user_input = int(user_input("Please enter your code (0-5):  "))
# if user_input <= 2:
#         print('Beginner')
# if user_input >= 3 < 4:
#         print("Intermediate")
# if user_input == 5:
#         print("Expert")

# solution
        
def checker():
        user_input = int(input("Please enter your code (0-5):  "))
        
        if user_input <= 2:
                print("Beginner")
        elif user_input >= 3 and user_input <= 4:
                print("Intermediate")
        else:
                print("Expert")
                
checker()


# 10. Write a function called 'python_experience'.
# It should take your name and return your python experience in the form below
# '{name} python experience is awesome'

def python_experience(name):
     return(f"{name}'s python experience is awesome")  
        
# name = ("shalom") # ❌

python_experience("Shalom")