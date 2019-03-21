#SIMPLE FUNCTIONS


# def do_nothing():
#     pass

# def do_something():
#     print("My first function")

# def say_hello():
#     print("Hello world")

# do_nothing()
# do_something()
# do_something()


# name = ["omotayo", "tolu", "chidi", "femi", "shade"]
# def greet(class_attendance):

#     print("Hello", class_attendance)
# for class_attendance in name :
    
#     greet(class_attendance)


# name = ["omotayo", "tolu", "chidi", "femi", "shade"]
# age = [18, 19, 20, 21, 22]

# def greet(name, age):
#     computer_age = 20

#     if computer_age < age :
#         print("e kaabo", name)
#     else:
#         print("kaabo", name)
# for x,y in zip(name, age) :
    
#     greet( x,y)

# ages = [2, 3, 4, 5]
# total_ages = sum(ages)

# print(total_ages)

# # ages_1= [2, 3, 4, 5]
# # ages_2 = [6, 7, 8, 9]
# # ages_3 = [16, 71, 14, 13]

# # def sum (ages_1, ages_2, ages_3):
# #    total = (ages_1 * ages_2)
# #    print(total)
# # for x,y in zip(ages_1, ages_2):
#     sum(x,y)


# ages_1= [2, 3, 4, 5]
# ages_2 = [6, 7, 8, 9]
# ages_3 = [16, 71, 14, 13]

# def sum (ages_1, ages_2, ages_3):
#    total = (ages_1 * ages_2 * ages_3)
#    print(total)
# for x,y,z in zip(ages_1, ages_2, ages_3):
#     sum(x,y,z)



# ages_1= [1, 2, 3, 4, 5]

# def sum_of_ages(_list):
#     sum = 0
#     for item in _list:
#         sum += item
#     print("the sum of", _list, "is",sum)
# sum_of_ages([1, 2, 3, 4, 5])

# ages_1= [1, 2, 3, 4, 5]

# def sum_of_ages(_list):
#     sum = 0
#     if isinstance(_list, list):
#         for item in _list:
#             sum += item
#         print("the sum of", _list, "is",sum)
#     else:
#         print(type(_list), "is not a list")
# sum_of_ages([1, 2, 3, 4, 5])
# sum_of_ages(1)



# products = dict(
#     beans = 100,
#     rice =200,
#     garri = 300,
#     meat = 400,
#     poundo = 150,
#     pork = 250
#  )

# def sum_of_products_prices(_dict):
#     sum = 0
#     for key in _dict:
#         sum += _dict[key]
#     print(sum)

# sum_of_products_prices(products)


    
# products = dict(
#     beans = 100,
#     rice =200,
#     garri = 300,
#     meat = 400,
#     poundo = 150,
#     pork = 250
#  )

# def sum_of_prices(_dict):
#     sum = 0
#     if isinstance(_dict, dict):
#         for key in _dict:
#             sum += _dict[key]
#         print("the sum of", _dict, "is", sum)
#     else:
#         print(type(_dict), "is not a dict")

# sum_of_prices(products)


# products = dict(
#     beans = 100,
#     rice =200,
#     garri = 300,
#     meat = 400,
#     poundo = 150,
#     pork = 250
#  )

# def sum_of_prices(_dict):
#     sum = 0
#     if isinstance(_dict, dict):
#         for key in _dict:
#             sum += _dict[key]
#         print("the sum of is", sum)
#     else:
#         print(type(_dict), "is not a dict")

# sum_of_prices(products)

# print(26,2,19, sep ="/", end= ".")


#this program shows the maximum value of a list or two two values


# def max_val(x,y):
#     if x > y:
#         return x
#     elif y > x :
#         return y
#     else:
#         return "no greater value"
# print(max_val(45,65))

# def max_leghth(x,y):
#     if len(x) > len(y):
#         return x
#     elif len(y) > len(x) :
#         return y
#     else:
#         return "no greater value"
# print(max_leghth("toun", "omotayo"))  


# num1 = int(input("pls input a number: "))
# num2 = int(input("pls input a number: "))
# den1 = int(input("pls input a number: "))
# den2 = int(input("pls input a number: "))
# def fraction(num1, den1, num2, den2): 

#     new_num =(num1*den2) +(num2*den1)   
#     new_den = den1*den2

#     print("the sum is: ", str(new_num) +"/"+str(new_den) )
# fraction(num1, den1, num2, den2)

def fraction(num1, den1, num2, den2):
    fraction = int(input("pls input all fractions: "))
    print("the sum is: ",   )   