#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
# Timeit desabilita o 'Garbage Collection' para que este não interfira no resultado
# https://docs.python.org/dev/library/timeit.html
# https://pt.stackoverflow.com/questions/97364/medir-o-tempo-de-execu%C3%A7%C3%A3o-de-uma-fun%C3%A7%C3%A3o

#Função Insertion Sort
def insertionSort(arr):
    #Percorre de 1 até len(arr)(arranjo)
    for i in range(1, len(arr)):
        chave = arr[i]

        #Move os elementos de arr[0...i-1], que são
        #maiores que a chave, para uma posição a frente
        #da posição atual
        j = i -1
        while j >=0 and chave < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = chave
    return arr

##Função Main
def main():
    arr = 'entrada1e+06.txt'
    arr = open(arr, 'r')
    li = arr.readlines()
    #Essa parte irá contar quanto tempo foi gasto na execução do algoritmo
    tempinicial = timeit.default_timer()
    arr = insertionSort(li)
    tempfinal = timeit.default_timer()
    print('duracao: %f' % (tempfinal - tempinicial))
    print(arr)


if __name__ == "__main__":
    main()