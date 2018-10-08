#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import timeit


# Merges dois subarrays de arr[].
# Primeiro subarray é arr[l..m]
# Segundo subarray é arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # criação de arrays temporárias
    L = [0] * (n1)
    R = [0] * (n2)

    # Copia a data para os arrays temporários L[] e R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # Merge os arrays temporários de volta para arr[l..r]
    i = 0  # Index inicial do primeiro subarray
    j = 0  # Index inicial do primeiro subarray
    k = l  # Index inicial do subarray "merged"

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copia os elementos restanto em L[], se tiver algum
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    #
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l é para o index esquerdo e r é para o index direito do sub-array que será
# ordenado
def mergeSort(arr, l, r):
    if l < r:
        # O mesmo para (l+r)//2, mas evita overflow para
        # l e h grandes
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


    ##Função Main
def main():
    #Arquivo para teste
    arquivo = open('entrada-aleatorio-10.txt', 'r')
    dados = arquivo.read()
    elementos = [int (i) for i in dados.split()]
    print('\tTamanho: ',len(elementos))
    print('\nSEM ORDENAR -> ', elementos)
    n = len(elementos)
    #Essa parte irá contar quanto tempo foi gasto na execução do algoritmo
    tempinicial = timeit.default_timer()
    mergeSort(elementos, 0, n-1)
    tempfinal = timeit.default_timer()
    print('\nDEPOIS DE ORDENAR -> ', elementos)
    print('\n\t\tDuracao: %f' % (tempfinal - tempinicial))


if __name__ == "__main__":
    main()