#Education part

#print (123%10)
#======================
#a = 15 // (16 % 7)
#b = 34 % a * 5 - 29 % 5 * 2
#print(a + b)
#======================

#a = 82 // 3 ** 2 % 7
#print(a)

#Practice:

#1 Geometric progression:

#bn = b^1 * q^(n-1)

#b1 = int(input())
#q = int(input())
#n = int(input())

#progression = b1 * q**(n-1)

#print (progression)

#2 Distance in meters:

#Input data format
#The input to the program is a natural number - the number of centimeters.
#Output data format
#The program should output one number - the total number of meters.

#Sample Input 1:
#345
#Sample Output 1:
#3

#cm = int(input())

#print (cm//100)

#3 Mandarins:

#n pupils are divided k tangerines equally, the undivided remainder remains in the basket. How many whole tangerines will each student get? How many whole tangerines will remain in the basket?

#Input data format
#The program receives two integers as input: the number of schoolchildren and the number of tangerines, each on a separate line.

#Output data format
#The program should output two numbers: the number of tangerines that each student will get and the number of tangerines that will remain in the basket, each on a separate line.

#pupils = int(input())
#tangerines = int(input())

# print (tangerines // pupils)
# print (tangerines % pupils)

# 4 Avengers is back

# The mad titan Thanos has collected all 6 infinity stones and intends to wipe out half the population of the universe at the snap of his fingers. 
# If the population of the universe is an odd number, the titan will show mercy and round up the number of survivors. Help the Avengers count the number of survivors.

# population = int(input())
# survivors = (population // 2) + population % 2
# print (survivors)

# 5 train compartments

# The compartment train has 
# 9 compartments with four seats for passengers in each compartment. 
# Write a program that determines the number of the compartment where the seat with the given number is located (the numbering of seats is through, starting from 1).

number_of_seat = int(input())
number_of_seat = number_of_seat * -1
print (number_of_seat // 4 * -1)