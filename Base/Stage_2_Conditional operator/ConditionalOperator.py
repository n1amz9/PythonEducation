# i = int(input())
# if i % 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')

#==================================

# When registering on websites, you are required to enter your password twice. This is done for security, as this approach reduces the possibility of incorrect password entry.

# Write a program that compares the password and its confirmation. If they match, the program outputs: "Password accepted", otherwise: "Password not accepted".

#==================================

# password = input()
# check_password = input()

# if password == check_password :
#     print ('Пароль принят')
# else :
#     print ('Пароль не принят')

#==================================

# number = int(input())

# if (number % 2 == 0) :
#     print ("Четное")
# else :
#     print ("Нечетное")

#==================================

# number = int(input()) # 1614
# n0 = number // 1000
# n1 = number // 100 % 10
# n2 = number // 10 % 100 % 10
# n3 = number % 1000 % 100 % 10

# if n0 + n3 == n1 - n2 :
#     print ('ДА')
# else :
#     print('НЕТ')

#==================================

# age = int(input())

# if age >= 18:
#     print ("Доступ разрешен")
# else :
#     print ("Доступ запрещен")

#==================================

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# if num2 - num1 == num3 - num2:
#     print ('YES')
# else :
#     print ('NO')

#==================================

# num1 = int(input())
# num2 = int(input())

# if num2 < num1:
#     print (num2)
# else :
#     print (num1)

#==================================

# 1 2 3 4
# 1 < 2 < 3 < 4

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# a = 0
# b = 0

# if num1 < num2 :
#     a = num1
# else :
#     a = num2

# if num3 < num4:
#     b = num3
# else :
#     b = num4
    
# if a < b :
#     print (a)
# else:
#     print (b)

# print (min(num1,num2,num3,num4)) not fair

#==================================

# print ("Введите свой полный возраст:", end="\n")
# age = int(input())

# if age <= 13:
#     print("детство")
# if 14 <= age <= 24:
#     print ("молодость")
# if 25 <= age <= 59:
#     print ("зрелость")
# if age >= 60 :
#     print ("старость")

#==================================

# num1, num2, num3 = int(input()), int(input()), int(input())
# sum = 0

# if (num1 >= 0) :
#     sum = sum + num1
# if (num2 >= 0) :
#     sum = sum + num2
# if (num3 >= 0) :
#     sum = sum + num3
# print (sum)

#==================================

# a = int(input())

# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5

# p = (a + b) * (a + b)
# print(p)

#==================================

# num = int(input())

# if -1 < num < 17 :
#     print ("Принадлежит")
# else:
#     print ("Не принадлежит")

#==================================

# num = int(input())

# if num <= -3 or num >= 7 :
#     print ("Принадлежит")
# else :
#     print ("Не принадлежит")

#==================================

# num = int(input())

# if (-30 < num <= -2) or (7 < num <= 25) :
#     print ("Принадлежит")
# else :
#     print ("Не принадлежит")

#==================================

# num = int(input())

# if (num // 1000 > 0 and num // 1000 < 10) and (num % 7 == 0 or num % 17 == 0) :
#     print ("YES")
# else :
#     print ("NO")
    
#==================================

# # a+b>c
# # a+c>b
# # b+c>a,

# a = int(input())
# b = int(input())
# c = int(input())

# if (a + b > c) and (a+c>b) and (b+c>a):
#     print ("YES")
# else : 
#     print ("NO")
    
#==================================

# year = int(input())

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print ("YES")
# else:
#     print ("NO")
    
#==================================

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# if (x1 == x2 and y1 != y2) or (y1 == y2 and x1 != x2) :
#     print ("YES")
# else :
#     print ("NO")
    
#==================================

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# if (-1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1) :
#     print ("YES")
# else:
#     print ("NO")
    
#==================================

# zum_speed = int(input())
# flash_speed = int(input())

# if (zum_speed > flash_speed) :
#     print ("NO")
# elif (zum_speed < flash_speed):
#     print ("YES")
# else:
#     print ("Don't know")
        
#==================================

# a = int(input())
# b = int(input())
# c = int(input())

# if (a == b and c != b) or (b == c and a != c) or (a == c and b != c) :
#     print ("Равнобедренный")
# elif a == b == c :
#     print ("Равносторонний")
# else :
#     print ("Разносторонний")
            
#==================================

# 1 2 3

# a = int(input())
# b = int(input())
# c = int(input())

# min1 = 0 
# min2 = 0

# if (a > c and a < b) or (a > b and a < c): 
#         print (a)
        
# if (b > c and b < a) or (b > a and b < c) :
#         print (b)
        
# if (c > b and c < a) or (c > a and c < b) :
#         print (c)
            
#==================================

# 4,6,9,11 = 30
# 1,3,5,7,8,10,12 = 31
# 2 = 28

# month = int(input())

# if (month == 2) :
#     print ("28")
# if ((month == 4 or month == 6 or month == 9 or month == 11) and month == 2) : 
#     print ("30")
# else:
#     print ("31")
            
#==================================

# weight = int(input())

# if (weight < 60) :
#     print ("Легкий вес")
# elif (weight < 64):
#     print ("Первый полусредний вес")
# else:
#     print ("Полусредний вес")
            
#==================================

# Calculator moment

# a = int(input())
# b = int(input())
# s = str(input())

# if (b == 0 and s == "/") :
#     print ("На ноль делить нельзя!")
# elif (s == "+") :
#     print(a + b)
# elif (s == "-") :
#     print(a - b)
# elif (s == "*") :
#     print(a * b)
# elif (s == "/") :
#     print(a / b)
# else :
#     print ("Неверная операция")
            
#==================================

# colours mixer

# colour1 = str(input())
# colour2 = str(input())

# if (colour1 == colour2 and (colour1 == "синий" or colour1 == "желтый" or colour1 == "красный")) :
#     print (colour1)
# elif ((colour1 == "синий" and colour2 == "красный") or (colour1 == "красный" and colour2 == "синий")) :
#     print ("фиолетовый")
# elif ((colour1 == "красный" and colour2 == "желтый") or (colour1 == "желтый" and colour2 == "красный")) :
#     print ("оранжевый")
# elif ((colour1 == "желтый" and colour2 == "синий") or (colour1 == "синий" and colour2 == "желтый")) :
#     print ("зеленый")
# else :
#     print ("ошибка цвета")

#==================================

# lot = int(input())

# if (lot == 0) :
#     print ("зеленый")

# elif 1 <= lot <= 10 :
#     if (lot % 2 == 0):
#         print ("черный")
#     else :
#         print ("красный ")

# elif 11 <= lot <= 18 :
#     if (lot % 2 == 0) :
#         print ("красный")
#     else :
#         print ("черный ")

# elif 19 <= lot <= 28 :
#     if (lot % 2 == 0) :
#         print ("черный")
#     else :
#         print ("красный ")

# elif 29 <= lot <= 36 :
#     if (lot % 2 == 0) :
#         print ("красный")
#     else :
#         print ("черный ")

# else :
#     print ("ошибка ввода")
    
# ==============================

# segments check

# ex:
# a1 = 1 ; b1 = 3 
# a2 = 2 ; b2 = 4 

# ###****** a1; b1
# *###***** a2; b2 
# answer : a2; b1

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())

# if (a1 == a2) :
#     if (b1 == b2) :
#         print (a1, b2)
#     elif (b1 > b2) :
#         print (a2, b2)
#     elif (b1 < b2) :
#         print (a2, b1)
        
# if (a1 > a2) :
#     if (b1 == b2) :
#         print (a1, b1)
#     elif (b1 < b2) :
#         print (a1, b1)
#     elif (b1 > b2):
#         if (b2 > a1) :
#             print (a1, b2)
#         elif (a1 == b2) :
#             print (a1)
#         else:
#             print ("пустое множество")    
    
    
# if (a1 < a2) :
#     if (b1 == b2) :
#         print (a2, b2)
#     elif (b1 > b2) :
#         print (a2, b2)
#     elif (b1 < b2) :
#         if (a2 < b1):
#             print (a2, b1)
#         elif (b1 == a2) :
#             print (b1)
#         else :
#             print ("пустое множество")

# ==============================