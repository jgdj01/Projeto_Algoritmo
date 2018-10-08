#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Créditos pela função shell:
# https://rosettacode.org/wiki/Sorting_algorithms/Shell_sort#Python

import sys
import timeit
import math

def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

#Função Main
def main():
    # Arquivo para teste
    arquivo = open('entrada-decrescente-1000000.txt', 'r')
    dados = arquivo.read()
    elementos = [int(i) for i in dados.split()]
    print('\tTamanho: ', len(elementos))
    #print('\nSEM ORDENAR -> ', elementos)
    # Essa parte irá contar quanto tempo foi gasto na execução do algoritmo
    tempinicial = timeit.default_timer()
    shell(elementos)
    tempfinal = timeit.default_timer()
    print('\nDEPOIS DE ORDENAR -> ', elementos)
    print('\n\t\tDuracao: %f' % (tempfinal - tempinicial))

if __name__ == "__main__":
    main()



