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

class Marriage:
    
    def __init__(self, husband, wife):
        self.husband = husband
        self.wife = wife
        
    def couple(self):
        tt = f"{self.husband} is the husband and {self.wife} is the wife"
        # print(tt)
        return(tt)
    
k = Marriage("olawale", "shasha baby")
p = k.couple()
print(p)
y1 = k.husband
y2 = k.wife
print(y1, y2)
   
    
       