import os
import time

'''1. Escreva uma função recursiva em Python que calcule a soma dos primeiros N
números inteiros positivos.'''


def soma_dos_numeros(numero):
    # Caso base
    if numero <= 0:
        return 0
    # chamada recursiva
    return numero + soma_dos_numeros(numero - 1)


numero_digitado = int(input('Digite um Numero INTEIRO: '))

somas = soma_dos_numeros(numero_digitado)
print(F'A SOMA DOS NUMEROS É {somas}')
time.sleep(2)
os.system('cls')


'''
2. Escreva uma função recursiva para calcular o número fatorial de um número inteiro
positivo.
3. Escreva uma função que use uma pilha para inverter uma string.
4. Escreva uma função que converte um número decimal em sua representação binária
usando uma pilha.
5. Implemente um histórico de comandos de um editor de texto simples usando uma
pilha. A cada vez que um comando é executado, ele é adicionado à pilha.
Implemente a capacidade de desfazer um comando usando a pilha.'''
