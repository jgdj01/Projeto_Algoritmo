#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import timeit
# Timeit desabilita o 'Garbage Collection' para que este não interfira no resultado
# https://docs.python.org/dev/library/timeit.html
# https://pt.stackoverflow.com/questions/97364/medir-o-tempo-de-execu%C3%A7%C3%A3o-de-uma-fun%C3%A7%C3%A3o


#Função Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        #Percorre todo o array
        for j in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
    #Troca o elemento minimo com
    #o primeiro elemento
    arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#Função Main
def main():
    arr = 'entrada1000.txt'
    arr = open(arr, 'r')
    li = arr.readlines()
    # Essa parte irá contar quanto tempo foi gasto na execução do algoritmo
    tempinicial = timeit.default_timer()
    arr = selection_sort(li)
    tempfinal = timeit.default_timer()
    print('duracao: %f' % (tempfinal - tempinicial))
    print(arr)

if __name__ == "__main__":
    main()