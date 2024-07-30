import random


def check_input(x): ## Проверка числа
    inp = input("Введите число: ")
    inp = int(inp)
    if (inp != x):
        if (inp > x):
            print(f"Ваше число больше загаданного числа на {inp - x}. Попробуйте ещё раз!")
            check_input(x)
        elif (inp < x):
            print(f"Ваше число меньше загаданного числа на {x - inp}. Попробуйте ещё раз!")
            check_input(x)
    else:
        print("Угадали!")

def start_function(ran_number): ## Начало игры
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

def main(): ## main XD
    check_input(start_function(0))

if __name__ == "__main__":
    main()
