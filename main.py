# import random
# num = random.randint(1, 10)

# guess = int(input("Введите число от 1 до 10: "))


# while num != guess:
#     if guess > 10:
#         print("Your number must be less than 10")
#     elif guess < 1:
#         print("Your number must be more than 10!")
#     guess = int(input("Try again! "))
# else:
#     print("Keep your cash")

# size = 10
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index = 0
# temp = 0

# while index < size/2:
#     temp = array[index]
#     array[index] = array[size - 1 - index]
#     array[size - 1 - index] = temp
# index =+ 1

# print(array)
# number = [1, 2, 3, 4, 5]
# print(type(number))

# for i in range(5):
#     print(i ** 2)

# words = "Hello, World!"

# for word in words:
#     print(ord(word), word)

# fruits = ["Banana", "Apple", "Strawberry", "Vine", "Grape"]

# for fruit in fruits:
#     print(fruit[0])

# numbers = [2, 3, 4, 5]
# for number in numbers:
#     for i in range(1, 11):
#         print(f"{number} x {i} = {number * i}")

# lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for list in lists:
#     for item in list:
#         print(item)

# rows = [0, 1, 2, 3]
# columns = [0, 1, 2, 3, 4]

# for row in rows:
#     for column in columns:
#         print(f"{row} and {column}")

# words = ["Hello", "Duman", "and", "Dina"]

# for word in words:
#     count = 0
#     vowels = "aeiou"
#     for i in word:
#         if i in vowels:
#             count += 1
#     print(f"Number of vowels in {word} : {count}")

# even_numbers = []
# for i in range(2, 11, 2):
#     even_numbers.append(i)
# print(even_numbers)

# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)
