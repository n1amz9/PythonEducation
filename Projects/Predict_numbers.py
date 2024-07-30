import random


def check_input(x):
    inp = input("Введите число: ")
    inp = int(inp)
    if (inp != x):
        print("Почти)")
    else:
        print("Угадали!")

def start_function(ran_number):
    print("Вас приветствует игра в угадайку :)")
    print("\n")
    min_num = input("Введите минимальное число для генерации: ")
    max_num = input("Введите максимальное число для генерации: ")
    min_num = int(min_num)
    max_num = int(max_num)
    
    print("\n")
    ran_number = random.randint(min_num, max_num)
    print(ran_number)
    print(f"Загадали число от {min_num} до {max_num}. Попробуйте его угадать)")
    return ran_number

def main():
    check_input(start_function(0))

if __name__ == "__main__":
    main()
