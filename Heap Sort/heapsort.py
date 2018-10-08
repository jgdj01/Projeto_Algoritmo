#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import timeit

# Créditos para:
# https://www.geeksforgeeks.org/heap-sort/
# Mohit Kumra

# Para "heapify" a subarvore raiz do indice i.
# n é o tamanho do heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # Verifica se a esquerda o filho da raiz existe e se
    # é maior que a raiz
    if l < n and arr[i] < arr[l]:
        largest = l

    # Verifica se o filho da raiz direita existe e se
    # é maior que a raiz
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Muda a raiz, se necessário
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # A função principal para classificar uma matriz de determinado tamanho


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

def main():
    #Arquivo para teste
    arquivo = open('entrada-aleatorio-10.txt', 'r')
    dados = arquivo.read()
    elementos = [int (i) for i in dados.split()]
    print('\tTamanho: ',len(elementos))
    print('\nSEM ORDENAR -> ', elementos)
    #Essa parte irá contar quanto tempo foi gasto na execução do algoritmo
    tempinicial = timeit.default_timer()
    heapSort(elementos)
    tempfinal = timeit.default_timer()
    print('\nDEPOIS DE ORDENAR -> ', elementos)
    print('\n\t\tDuracao: %f' % (tempfinal - tempinicial))


if __name__ == "__main__":
    main()