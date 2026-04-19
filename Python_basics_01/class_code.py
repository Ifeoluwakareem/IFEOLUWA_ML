class BeautyFinder:
    
    # general class attributes
    
    long_legs = True
    long_nose = True
    
    # Instance attribute 
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
            print(f"Model {self.name} is not obese.")
            
class Gender(BeautyFinder):
    male = "MALE"
    female = "FEMALE"
    
olawale = BeautyFinder("Ife", 50, 20)

# ife.detect_beauty()
# ife.detect_obesity()    

gg = Gender("Shalom", 60, 10)                            
print(gg.male, gg.female)
gg.detect_beauty()
gg.detect_obesity