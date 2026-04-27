def checker():
        user_input = int(input("Please enter your code (0-5):  "))
        
        if user_input <= 2:
                print("Beginner")
        elif user_input >= 3 and user_input <= 4:
                print("Intermediate")
        else:
                print("Expert")
                
checker()

# for for loop
numbers = [1, 2, 3, 4, 5]
square_number = []
for num in numbers:
    square_number.append(num * num)

print(square_number)               