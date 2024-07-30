def calc(num1, num2, sign):
    try:
        match sign:
            case "+":
                print (f"Результат {num1} {sign} {num2} = {num1 + num2}" )
            case "-":
                print (f"Результат {num1} {sign} {num2} = {num1 - num2}" )
            case "*":
                print (f"Результат {num1} {sign} {num2} = {num1 * num2}" )
            case "/":
                print (f"Результат {num1} {sign} {num2} = {num1 / num2}" )
            case "%":
                print (f"Результат {num1} {sign} {num2} = {num1 % num2}" )
            case "^":
                print (f"Результат {num1} {sign} {num2} = {num1 ** num2}" )
            case _:
                print("Вы ввели неверный знак оператор, или тот, кто пока не поддержан. Попробуйте снова")
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
    except Exception as e:
        print (f"Произошла ошибка: {e}")
        
def check_nums(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def start():
    print("Приветствуем в самом 'продвинутом' калькуляторе")
    num1 = input("Введите первое число: ")
    if (check_nums(num1) == False):
        print("Вы ввели не числовое значение. Попробуйте снова")
        return None
    num2 = input("Введите второе число: ")
    if (check_nums(num2) == False):
        print("Вы ввели не числовое значение. Попробуйте снова")
        return None
    sign = input("Введите математический знак (поддержаны +-*.%^): ")
    return(int(num1), int(num2), sign)

def main():
    num1, num2, sign = start()
    calc (num1, num2, sign)
    
if __name__ == "__main__":
    main()