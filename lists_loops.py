# states = ['New York', 'New Jersey', 'Connecticut', 'California']
#
# # for variable in list_of_elements:
# #     repetitive code here
#
# for state in states:
#     print (f"Welcome to {state}!!")
#
# # refactoring (rename) >> Shift + F6
# print()
#
# pizzas = ['Pepperoni', '4 Cheese', 'Margarita']
# for pizza in pizzas:
#     print(f"I like {pizza} pizza!!!")
# print('I really love pizza!')
#
# print()
#
# for num in range(5): # from 0 to 4
#     print(f"My current number: {num}")
#
# for num in range(3, 6): # from 3 to 5
#     print(f"My current number from range(3, 6): {num}")
#
# print()
#
# numbers = list(range(5)) # numbers = [0,1,2,3,4]
# print(numbers)
# squares = []
# for num in range(5, 13):
#     num_sqr = num ** 2
#     # squares.insert(-1, num_sqr)
#     squares.append(num_sqr)
#     # print(num_sqr)
#     # print(squares)
#
# print(squares)
# squares = list()
# for num in range(5, 13):
#     squares.append(num**2)
# print(squares)
#
# print()
#
# numbers = [5, 78, 456, 127, 230, 6, 5]
# print(f"Min number from numbers: {min(numbers)}")
# print(f"Max number from numbers: {max(numbers)}")
# print(f"Sum number from numbers: {sum(numbers)}")
#
# squares = [num ** 2 for num in range(5, 14, 2)]
# print(squares)
#
# print()
#
# million = list(range(1, 1000001))
# print(min(million))
# print(max(million))
# print(sum(million))


# nums = [5, 78, 456, 127, 230, 6, 5]
# print(nums[0:3]) # indexes>> 0,1,2
# print(nums[3:]) # from 3rd index to the end
# print(nums[1:-2]) # from 1st index (second element) to third from the end
#
# name = 'John Doe'
# print(name[5:]) # from 5th index to the end
#
# new_nums = nums
# nums_copy = nums[:]
#
# print("#copying the list example")
# print(nums,new_nums,nums_copy)
# nums.append(5555)
# print(nums,new_nums,nums_copy)


# HW 4-6, 4-7, 4-8, 4-9, 4-10, 4-11, 4-12

#____________HOME WORK
#4-6
number=list(range(1,21))
for number in range (1,21,2):
    print(f'This is odd number from the range 1-20: {number}')

print()
#4-7
digital=list(range(3,31))
multi=[digital*3 for digital in range(3,31)]
print(multi)

print()
#4-8
num=list(range(1,11))
cube=[num**3 for num in range(1,11)]
print(cube)

print()
#4-9

#4-10
cars=['nissan', 'lada', 'opel', 'bmw', 'mercedes', 'porshe']
print(f"The first three items in the list are: ")
for car in cars [:3]:
    print(car.title())
print(f"Three items from the middle of the list are: ")
for car in cars [1:4]:
    print(car.title())
print(f"The last three items in the list are: ")
for car in cars [-3:]:
    print(car.title())

print()
#4-11
my_pizzas = ['Pepperoni', '4 Cheese', 'Margarita']
friends_pizzas=my_pizzas[:]
my_pizzas.append('Regular')
friends_pizzas.append('Cesar')
print(f'My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)
print()
print(f'My friends favorite pizzas are: ')
for pizza in friends_pizzas:
    print(pizza)

print()
#4-12
my_foods=['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f'My favorite foods are:')
for food in my_foods:
    print(food.title())
print()
print(f'My friends favorite food are:')
for food in friend_foods:
    print(food.title())