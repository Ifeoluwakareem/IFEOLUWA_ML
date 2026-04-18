phantom = ["white", "black", "pink"]

# for j in phantom:
#     print(f"i am {j}")
    
# l = 0
# while l < len(phantom):
#     print(f"I am {phantom[l]}")
#     l += 1
    

# def determined(resolution):
#     msg = f"i will never give {resolution}"
#     # print(msg)
#     return msg
   
# # determined("up")
# jj = determined("up")
# print(jj)

# class Marriage:
    
#     def __init__(self, husband, wife):
#         self.husband = husband
#         self.wife = wife
        
#     def couple(self):
#         tt = f"{self.husband} is the husband and {self.wife} is the wife"
#         # print(tt)
#         return(tt)
    
# k = Marriage("olawale", "shasha baby")
# p = k.couple()
# print(p)
# y1 = k.husband
# y2 = k.wife
# print(y1, y2)
   
    
# class Foundation:
#     def __init__(self, mountain):
#         self.mountain = mountain
        
#     def nemb(self):
#         jeb = f"House is on the  {self.mountain}"
#         print(jeb)
        
# h = Foundation("hill")
# k = h.nemb()
# w = h.mountain

# def colour(lols):
#     prt = f"The name is {lols}"
#     print(prt)
    
# colour("Blue")

# def house(building):
#     jj = f"It is on the {building}"
#     print(jj)
    
# house("Hill")   


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


# class attribute 


class BeautyFinder:
    
    # general class  attributes
    long_legs = True
    long_nose = True
    
    #Instance attribute
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
         
    
    def detect_beauty(self):
        if int(self.height) >= 20:
            print(f"Model {self.name} is very beautiful.")
        else:
            print(f"Model {self.name} is not beautiful.")
            
    def detect_obesity(self):
        if int(self.weight) >= 30:
            print(f"Model {self.name} is obese.")
        else:
            print(f"Model {self.name} is not obese.")
  
class Gender(BeautyFinder):
    male = "MALE"
    female = "FEMALE"
          
            
olawale=BeautyFinder("olawale", 10, 50)  
# print(
#     olawale.long_legs,
#     olawale.long_nose,
#     olawale.name,
#     olawale.height,
#     olawale.weight  
#     )

# olawale.detect_beauty()
# olawale.detect_obesity()

 
ife=BeautyFinder("Ife", 50, 20 )

# ife.detect_beauty()
# ife.detect_obesity()



gg = Gender("Shalom", 60, 10)
print(gg.male, gg.female)
gg.detect_beauty()
gg.detect_obesity()






        
        
    
    
    
    