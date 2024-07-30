import random


def check_input(x): ## Проверка числа
    inp = input("Введите число: ")
    inp = int(inp)
    if (inp != x):
        if (inp > x):
            if ((inp - x) >= 20) :
                print(f"Ваше число сильно больше загаданного числа (>20). Попробуйте ещё раз!")
                check_input(x)
            elif ((inp - x) <= 5) :
                print(f"Почти угадали. Ваше число чуть больше загаданного числа (>5). Попробуйте ещё раз!")
                check_input(x)
            else:
                print(f"Ваше число немного больше загаданного числа. Попробуйте ещё раз!")
                check_input(x)
        elif (inp < x):
            if ((x - inp) >= 20) :
                print(f"Ваше число сильно меньше загаданного числа (>20). Попробуйте ещё раз!")
                check_input(x)
            elif ((x - inp) >= 5) :
                print(f"Почти угадали. Ваше число меньше загаданного числа (>5). Попробуйте ещё раз!")
                check_input(x)
            else:
                print(f"Ваше число немного меньше загаданного числа(<20). Попробуйте ещё раз!")
                check_input(x)
    else:
        print(f"Угадали! Загаданное компьютером число было {x}")

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
