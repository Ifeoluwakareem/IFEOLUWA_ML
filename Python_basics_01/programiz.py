# # PYTHON LIST COMPREHENSION
# numbers = [1, 2, 3, 4, 5]
# #list comprehension to create new list
# doubled_numbers = [num * 2 for num in numbers]

# print(doubled_numbers)

# # [expression for item in list if condition == True]
# # Here,
# # for every item in list, execute the expression if the condition is True.
# # Note: The if statement in list comprehension is optional.

# # for for loop
# numbers = [1, 2, 3, 4, 5]
# square_number = []
# for num in numbers:
#     square_number.append(num * num)

# print(square_number)

# # for list comprehension
# numbers = [1, 2, 3, 4, 5]
# #create a new list using list comprehension
# square_numbers = [num * num for num in numbers]

# print(square_numbers)

# # Conditionals in List Comprehension
# # filtering even numbers from a list
# even_numbers = [num for num in range(1, 10) if num % 2 == 0]

# print(even_numbers)

# # Example: List Comprehension with String
# word = "python"
# vowels = "aeiou"

# # find vowel in the string "Python"
# result = [char for char in word if char in vowels]

# print(result)

def checker():
        user_input = int(input("Please enter your code (0-5):  "))
        
        if user_input <= 2:
                print("Beginner")
        elif user_input >= 3 and user_input <= 4:
                print("Intermediate")
        else:
                print("Expert")