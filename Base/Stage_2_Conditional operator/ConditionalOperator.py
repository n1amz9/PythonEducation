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

num = int(input())

if -1 < num < 17 :
    print ("Принадлежит")
else:
    print ("Не принадлежит")

#==================================

