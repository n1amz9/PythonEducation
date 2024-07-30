import string
import random
import secrets

alphabetLet = list(string.ascii_letters)
alphabetNums = list(string.digits)
alphabetSymb = list(string.punctuation)


def passwordGenerator(bits):
    passw = []
    i = 0 
    while i < bits:
        try: 
            rand1 = random.randint(1, 3)
            match rand1:
                case 1: ## Letters
                    ran = random.randint(0, len(alphabetLet))
                    passw.append(alphabetLet[ran])
                    i+=1
                case 2: ## Numbers
                    ran = random.randint(0, len(alphabetNums))
                    passw.append(alphabetNums[ran])
                    i+=1
                case 3: ## Symbols
                    ran = random.randint(0, len(alphabetSymb))
                    passw.append(alphabetSymb[ran])
                    i+=1
        except Exception as e:
            print (f"!ERROR! {e}")
    return passw

def start():
    print ("Welcome to Password Generator")
    while True:
        try: 
            bits = input ("Please, specify the number of bits in the password: ")
            if (int(bits) < 8):
                raise ValueError("Password length must be at least 8.")
            print("Please, hold here for few seconds. Password generating now.")
            return bits
        except Exception as e:
            print (f"!ERROR!: {e}")

def main():
    print (f"Ваш пароль: {"".join(passwordGenerator(int(start())))}")

if __name__ == "__main__" :
    main()