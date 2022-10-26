import math
import random

qt = 2

while qt <= 10000000:
    arquivo_crescente = open(f'arquivos/{qt}-crescente.txt', 'w')
    for i in range(0, qt):
        arquivo_crescente.write(f'{i}\n')
    arquivo_crescente.close()

    arquivo_decrescente = open(f'arquivos/{qt}-decrescente.txt', 'w')

    for i in range(qt, 0, -1):
        arquivo_decrescente.write(f'{i}\n')
    arquivo_decrescente.close()


    arquivo_aleatorio = open(f'arquivos/{qt}-aleatorio.txt', 'w')


    
    aleatorios = [int(a) for a in open(f'arquivos/{qt}-decrescente.txt').read().split('\n') if a != '']
    random.shuffle(aleatorios)

    for numero in aleatorios:
        arquivo_aleatorio.write(f'{numero}\n')
    arquivo_aleatorio.close()



    qt *= 2
