# characteristics of a class
# 1. Inheritance --> A class sharing attr/method from a parent class

# 1️⃣ Encapsulation
# Bundling data (attributes) and methods (functions) together
# Restricts direct access to data
# 2️⃣ Abstraction
# Hides complex details
# Shows only what is necessary
# 3️⃣ Inheritance
# One class can inherit properties from another class
# Promotes code reuse
# 4️⃣ Polymorphism
# Same method name, different behavior
# Example: different classes using the same method differently
# 5️⃣ Modularity
# Code is organized into separate classes
# Makes programs easier to manage and reuse

#class attribute

# class BeautyFinder:
    
#     # general class attributes
    
#     long_legs = True
#     long_nose = True
    
#     #Instance attribute
#     def __init__(self, name, height, weight):
#         self.name = name
#         self.height = height
#         self.weight = weight
        
#     def detect_beauty(self):
#         if int(self.height) >= 20:
#             print(f"Model {self.name} is very beautiful.")
#         else:
#             print(f"Model {self.name} is not beautiful.")
            
#     def detect_obesity(self):
#         if int(self.weight) >= 30:
#             print(f"Model {self.name} is obese.")
#         else:
#             print(f"Model {self.name} is not obese.") 
            
# class Gender(BeautyFinder):
#     male = "MALE"
#     female = "FEMALE"
    
# olawale = BeautyFinder("olawale", 10, 50) 
# # print(
# #     olawale.long_legs,
# #     olawale.long_nose,
# #     olawale.name,
# #     olawale.height,
# #     olawale.weight
# #     )

# ife = BeautyFinder("Ife", 50, 20)

# ife.detect_beauty()
# ife.detect_obesity()

# gg = Gender("Shalom", 60, 10)
# print(gg.male, gg.female)
# gg.detect_beauty()
# gg.detect_obesity()

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Meow")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         (f"I am a dog. My name is {self.name}. I am {self.age} years old.")
print
#     def make_sound(self):
#         print("Bark")


# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()
