#calculadora
num1 = input('digite um numero: ')
num2 = input('digite outro numero: ')

if num1.isdigit() and num2.isdigit():#o isdigit seria para realizar contas somente com numericos checagem
    num1 = int(num1)
    num1= int(num2)
    
    print(num1 + num2)
else:
    print('não pude converter os numeros para realizar contas')    