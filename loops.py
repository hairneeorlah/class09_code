# for x in "banana":
#     print(x)
# for y in "technology":
#     print(y)

# _list = (1,2,3,4,5) #SAME AS RANGE(1,5)
# for i in range(1,5):
#     print(i)


# _list = (1,2,3,"banana",5) #SAME AS RANGE(1,5)
# for element in _list:
#     print(element)
#     for letter in str(element):
#         print(letter)

# _list = (1,2,3,"banana",5) #SAME AS RANGE(1,5)
# count = 0

# for element in _list:
#     print(element)
#     count += 1

# if str(element).isalpha():
#     for letter in (element):
#         print(letter)

# print("total count is", count)

# name = input("please enter your name:")
# count = 0

# for characters in name:
#     count +=1
# print("the total characters in your name is", count)
 
# password = 3333

# for i in range(9999):
#     print("testing", i, "--->", i == password)
#     if password == i:
#         print("your password is ", i)
#         break
# ASSSIGNMENT ON EXHAUSTIVE ENUMERATION

# blue = 100
# white = 80
# pink = 5
# answer = (blue+ white + pink) *3
# print(answer)
# for i in range(000,999):
#     print("testing", i, "--->", i==answer)
#     if answer == i:
#         print("the sum of sll values is", i)
#         break

# blue = 100
# white = 80
# pink = 5
# answer = (blue+ white + pink) +  (blue+ white + pink) + (blue+ white + pink)
# print(answer)
# for i in range(000,999):
#     print("testing", i, "--->", i==answer)
#     if answer == i:
#         print("the sum of all values is", i)


# blue = 100
# white = 80
# pink = 5
# answer = (blue+ white + pink) +  (blue+ white + pink) + (blue+ white + pink)
# print(answer)
# for i in range(000,999):
#     print("testing", i, "--->", i==answer)
#     if answer == i:
#         print("the sum of all values is", i)
#         break
        
        # WHILE LOOPS
# index = 0
# name = "adaku"
# while index < 5:
#     print(name[index])
#     index += 1


# py_class_students = ""
# response = ""

# while response != "end":
#     response = input("please enter your name: ")
#     if response == "end":
#         break
#     py_class_students += response if  len(py_class_students) == 0 else "," + response

# print(py_class_students)



# py_class_students = ""
# response = ""

# while True:
#     response = input("please enter your name: ")
#     if response == "end":
#         break
#     py_class_students += response if  len(py_class_students) == 0 else "," + response

# print(py_class_students)

# while True:
#     word = input(" pls enter a word : ")
#     new_word = list(word)
#     new_word.reverse() 
#     reveresd_and_joined = "".join(new_word)
#     if word == "clay":
#       break
#     print(reveresd_and_joined)
#     if word == reveresd_and_joined:
#         print(" this is a palidrome ")
#     else:
#         print(" this is not a palindrome")
    


