
#  stack = [] create an empty list called stack

#  def push(val):  create a function names push, and it takes one value(val)
#      stack.append(val) add the value to the end of the list
    
#  def pop():  create a function named pop
#      val = stack[-1]  get the last item in the list(top of the stack)
#      del stack[-1]  remove the last item from the list
#      return val   retun the removed value

#  push(3) add 3[3]
#  push(2) add 2[3, 2]
#  push(1) add 1[3, 2, 1]
#  print(pop()) remove and print 1
#  print(pop()) remove and print 2
#  print(pop()) remove and print 3
    

  
# family = ["Father", "Mother", "Sister", "Uncle", "Aunt", "Nephew", "Niece"]
# for n in family:
#     print(n)
    
# j = 0
# while j < len(family):
#     print(family[j])
#     j += 1
    
# class FullName:
    
#     def __init__(self, name, dog):
#         self.name = name
#         self.dog = dog
        
#     def namet(self):
#         ret_name = f"My name is {self.name}"
#         print(ret_name)
#         return ret_name   
    
#     def name_doggy(self):
#         ret_name = f"My name is {self.name} and my dog's name is {self.dog}"
#         print(ret_name)
#         return ret_name
    
# FullNameInstance =FullName("Samuel", "Bluey")
# my_name = FullNameInstance.namet()  
# my_name_dog = FullNameInstance.name_doggy()

# name_name = FullNameInstance.name
# print(name_name)

# dog_name = FullNameInstance.dog
# print(dog_name)


genders_array = ["Gay", "Straight", "Female"]
def gender_identity(identify):
    identify = input("Please identify yourself: ")
    print(f"Your identity is {identify}")
    
    
for i in genders_array:
    print(f"I am still investigating {i}")
    gender_identity(i)
    
    
    j = 0
    while j < len(genders_array):
        print(f"I am working on {genders_array[j]}")
        gender_identity(genders_array[j])
        j += 1