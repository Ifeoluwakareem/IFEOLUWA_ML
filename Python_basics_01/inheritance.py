from phantom_shalom import Gender

#abstraction: hiding code

#case1

def ifeoluwa():
    print("yaaaaaay")
    
ifeoluwa()

# case 2
# case hides absstraction/code 

kk = Gender("Ifeoluwa", 60, 15)
kk.detect_beauty()
kk.detect_obesity()
print(kk.male)    