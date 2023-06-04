"""Faça um programa que peça ao usuário para digitar um numero inteiro, 
informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é número inteiro."""

num1 = input('Digite um numeor inteiro: ')

if not num1.isdigit():
    print('Não é um numero inteiro')
else:
    num1 = int(num1)
if not num1 % 2 == 0:
    print(f'{num1} é ímpar')
else:
    print(f'{num1} é par')