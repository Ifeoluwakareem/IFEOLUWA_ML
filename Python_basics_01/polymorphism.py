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
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
        
#     def make_sound(self):
#         print("Bark")
        
        
# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()
                                    
class Cow:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a cow. My name is {self.name}. I am {self.age} years old.")
        
    def make_sound(self):
        print("Moo")
        
class Sheep:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a sheep. My name is {self.name}. I am {self.age} years old.")
        
    def make_sound(self):
        print("Baa")
        
cow1 = Cow("Cowboy", 7.8)
sheep1 = Sheep("Wooly", 6)

for animal in (cow1, sheep1):
    animal.make_sound()
    animal.info()
    animal.make_sound()                            
                                
   