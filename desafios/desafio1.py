"""
* criar variáveis para nome (str), idade (int)
*altura (float) e peso(float) de uma pessoa
*criar variável com o ano atual (int)
*obter o ano de nascimento da pessoa(baseado na idade e no ano atual)
*obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
*exibir um texto com todos os valores na tela usando f-strings (com as chaves)
"""
nome = 'Thalía'
idade = 21
altura = 1.55
peso = 60
ano_atual = 2023
nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos e nasceu em {nascimento} e seu imc é {imc: .2f}')
