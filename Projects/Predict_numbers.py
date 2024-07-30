import random


def check_input(x):
    return None

def main():
    number = random.randint(0, 50)
    input = -100
    
    print("Вас приветствует игра в угадайку :)")
    print("\n")
    min_num= input("Введите минимальное число для генерации: ")
    max_num= input("Введите максимальное число для генерации: ")
    
    print (min_num)
    print (max_num)
    print(number)
    
if __name__ == "__main__":
    main()
