import sys

def sum(self, x,y):
    return x+y

def subtraction(self, x,y):
    return x-y

def multiplication(self, x,y):
    return x*y

def division(self, x,y):
    return x/y if y != 0 else None

def main():
    if len(sys.argv) != 4:
        print("python3 calculadora.py <operação> <número1> <número2>")
        return

    operacao = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operacao == '1':
        print("Result:", sum(num1, num2))

    elif operacao == '2':
        print("Result:", subtraction(num1, num2))

    else:
        print("Invalid")

if __name__ == "__main__":
    main()