

# # print('my first hello word!')
# # print("hello future python programmer!")

# Module: A single Python file (.py) that contains code (functions, variables, classes).
# Package: A folder that contains multiple modules (and possibly sub-packages), used to organize code.
# Class: A blueprint for creating objects; it defines attributes and methods.
# instance: a child of a class

# import math
# # print(math.__dir__()) # exposes the methods in the package
# print(math.sin(90))
# print(math.log2(90))


# import os
# print(os.__dir__())
# print(dir(os))
# os.mkdir("my_new_directory_2")
# print(os.listdir())




# def full_name(last_name, dog):
#     full_name_now = last_name + " " + dog
#     print(full_name_now)
    
# full_name("Kareem", "Bingo")




# class fullName:
    
#     #class initiation
#     def __init__(self, name, dog):
#         self.name = name
#         self.dog = dog

#     #class methods
#     def namet(self):
#         ret_name = f"My name is {self.name} "
#         print(ret_name)
#         return ret_name
    
#     def name_dog(self):
#         ret_name = f"My name is {self.name} and my dog's name is {self.dog} "
#         print(ret_name)
#         return ret_name


# fullNameInstance = fullName("kareem", "Bingo")   # instantiate class

# my_name = fullNameInstance.namet()
# my_name_dog =   fullNameInstance.name_dog()
# name_name = fullNameInstance.name
# print(name_name)
# dog_name = fullNameInstance.dog
# print(dog_name)




# class Flower:
#     stem = 'green'
#     def __init__(self, petals=True, thorns=False):
#         self.__petals = petals
#         self.__thorns = thorns

# flower = Flower(False)
# flower.__leaves = True
# print(flower.__dict__)
    




# class ExampleClass:
#     def __init__(self, val =1):
#         self.__first = val 
        
#     def set_second(self, val):
#         self.__second= val
        
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)

# example_object_2.set_second(3)

# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)          
        
# class Flower:
#     stem = 'green'
#     def __init__(self, petals=True, thorns=False):
#         self.__petals = petals
#         self.__thorns = thorns

# flower = Flower(False)
# flower.__leaves = True
# print(flower.__dict__)

# class Flower:
#     def __init__(self, petals=True, thorns=False):
#         self.__petals = petals
#         self.__thorns = thorns

# flower = Flower()
# flower.__leaves = True

# class Calculator:
#     base_value = 10
#     def add(self, first_value, second_value):
#         print(self.base_value + first_value + second_value)
        
# calc = Calculator()
# print(calc.add(1, 2))      

# class Dog:
#     def__init__(self, name)
#     self.name = name
        
#     def bark(self):
#             print("Woof")
            
# pet1 = Dog("Max")
# pet2 = Dog("Daisy")  

# print(Dog.__name__)
# print(type(pet1).__name__) 
# print(pet1.__module__)        

# class Dog:
#     def __init__(self, name, breed):  
#      self.name = name
#      self.breed = breed
     
#     def __str__(self):
#         return self.name + " is a " + self.breed    
     
# pet1 = Dog("Max", "Labrador")
# print(pet1)     

# for i in range(5):
#     print(i)
    
# for j in range(20):
#     print(j)    


# class CustomRange:
#     def __init__(self, range):
#         self.__range = range
#         self.__i = 0
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         res = self.__i
#         self.__i += 1
        
#         if self.__i > self.__range:
#             raise StopIteration
        
#         return res
    
# range = CustomRange(10)        
    
# for i in range:
#     print(i)   


# def my_range():
#     for i in range(5):
#      yield i           
        
        
# first_list = []

# for x in range(5):
#     first_list.append(10 ** x)
    
# print(first_list)

# second_list = [10 ** x for x in range(10)]
# print(second_list)   
 

# [x for x in range(10) if x % 2 == 0]

# stream = open("path/to/file", "r")

# data = bytearray(5)
# data[1] = 2

# for b in data:
#     print(hex(b))


# class FullName :
#     def __init__(self, name, dog):
#         self.name = name
#         self.dog = dog
        
#     def __str__(self):
#         return f"My name is {self.name} and my dog's name is {self.dog}"
    
# person = FullName("Kareem", "Bingo")   
# print(person)
    

# class FullName : #defines a class named FullName
#     def __init__(self, name, dog): #__int__ is a constructor method that automatically runs when an object is created, self is sthe object ,name and dog are the arguments.
#         self.name = name  #saves the passed name into the object
#         self.dog = dog    #saves the passed animal into the object
        
    
#     def __str__(self):  #special methos that controls what is shown when you print the object
#         return f"My name is {self.name} and my dogs's name is {self.dog}" #returns a formatted string using the object's data
    
# person = FullName("Habibat", "pecky") #Habibat goes into name and Pecky goes into dog(instanties)
# print(person)    #calls __str__ automatically and prints the formatted message
    
            
    
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

# class FullName:
    
#     def __init__(self, name, state):
#         self.name = name
#         self.state = state
        
        
#     def namet(self):
#         ret_name = f"My name is {self.name}" 
#         print(ret_name) 
#         return ret_name 
    
#     def name_state(self):
#         ret_name = f"My name is {self.name} and my state's name is {self.state}"
#         print(ret_name)
#         return ret_name
    
    
# FullNameInstance = FullName("Olanrewanju", "Lagos") 
# my_name = FullNameInstance.namet()
# my_name_state = FullNameInstance.name_state()
    
# name_name = FullNameInstance.name
# print(name_name)
    
# state_name = FullNameInstance.state
# print(state_name)
            
# class Family:
    
#     def __init__(self, complexion, height):  
#         self.complexion = complexion
#         self.height = height
        
#     def milet(self):
#         ret_complexion = f"My complexion is {self.complexion}"
#         print(ret_complexion)
#         return ret_complexion
    
#     def hitto(self):
#         ret_complexion =f"My complexion is {self.complexion} and my height is {self.height}"
#         print(ret_complexion)
#         return ret_complexion
    
# FamilyInstance = Family("Dark skinned", "Tall")
# my_complexion = FamilyInstance.milet()
# my_hitto = FamilyInstance.hitto()

# complexion_complexion = FamilyInstance.complexion
# print(complexion_complexion)

# hitto_hitto = FamilyInstance.hitto
# print(hitto_hitto)

                    
# class FullName:
#     def __init__(self, name, dog):
#         self.name = name
#         self.dog = dog
        
#     def namet(self):
#         ret_name = f"My name is {self.name}"
#         print(ret_name)
#         return ret_name
    
#     def name_dog(self):
#         ret_name = f"My name is {self.name} and my dog's name is {self.dog}"
#         print(ret_name)
#         return ret_name
    
# FullNameInstance = FullName("Haqq", "Dogmi")
# my_name = FullNameInstance.namet()
# my_name_dog = FullNameInstance.name_dog()

# name_name = FullNameInstance.name
# print(name_name)

# name_dog = FullNameInstance.dog
# print(name_dog)
       

class FullName:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog
        
    def namet(self):
        ret_name = f"My name is {self.name}"
        print(ret_name)
        return ret_name
    
    def name_dog(self):
        ret_name = f"My name is {self.name} and my dog's name is {self.dog}"
        print(ret_name)
        return ret_name
    
FullNameInstance = FullName("Kiara", "Jojo")
my_name = FullNameInstance.namet()
my_name_dog = FullNameInstance.name_dog()

name_name = FullNameInstance.name
print(name_name)

name_dog = FullNameInstance.dog
print(name_dog)          
