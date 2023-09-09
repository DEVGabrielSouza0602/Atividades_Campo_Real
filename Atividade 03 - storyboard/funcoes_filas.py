import os
import time


def limpesa_e_time(segundos):
    time.sleep(segundos)
    os.system('cls')


def apresentacao_de_dados(fila):
    print('Apresentação dos dados: ')
    for posicao, valor in enumerate(fila):
        print(
            f'Posicao do chamado = {posicao} | Nome do Usuario: {valor}', end=' | ')
        print('')
        time.sleep(1)


def inserir_com_prioridade(fila, prioridade_do_item, item):
    for i in lifilasta:
        ...


def remover_elemento_x(fila, indice):
    fila.pop(indice)


def remover_com_o_indice_desejado(fila, indice):
    if indice > -1:
        if indice <= len(fila):
            print('Removendo elemento...')
            remover_elemento_x(fila, indice)
            limpesa_e_time(2)
        else:
            print('INDICE NÃO EXISTE...')
            limpesa_e_time(2)
    else:
        print('INDICE INFERIOR A 0')
        limpesa_e_time(2)

# inserir dados no final da fila


def incersao_De_dados_enqueue(dado, fila):
    fila.append(dado)

# Remoção - no inicio


def remover_no_inicio_da_fila_dequeue(fila):
    if len(fila) == 0:
        limpesa_e_time(2)
        return "A fila está vazia, não é possível remover"
    else:
        limpesa_e_time(2)
        return fila.pop(0)

# Primeiro elemento - peek


def peek(fila):
    if len(fila) == 0:
        return "Fila vazia"
    else:
        return fila[0]

# retorna bool de fila esta vazia


def is_empty(fila):
    return len(fila) == 0

# retorna o tamanho da fila


def size(fila):
    return len(fila)

# Reverse


def puxa_o_ultimo_elemento_queuereverse(fila):
    filaReversa = []
   # return fila [::-1]
    while not is_empty(fila):
        item = fila.pop()  # dequeue(fila)
        incersao_De_dados(filaReversa, item)
    return filaReversa
