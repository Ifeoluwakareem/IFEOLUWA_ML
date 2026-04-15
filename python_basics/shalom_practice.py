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
    
genders_array = ["Gay", "Straight", "Female"]

for i in genders_array:
    print(f"I am working on {i}")
    gender_identity(i)
    
j = 0
while j < len(genders_array):
   print(f"I am working on {genders_array[j]}")  
   gender_identity(genders_array[j])  
   j += 1
    
    
    