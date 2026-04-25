def checker():
        user_input = int(input("Please enter your code (0-5):  "))
        
        if user_input <= 2:
                print("Beginner")
        elif user_input >= 3 and user_input <= 4:
                print("Intermediate")
        else:
                print("Expert")
                
checker()                