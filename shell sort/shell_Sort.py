#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import timeit
import math

def shellSort(arr):
    # Começa com uma lacuna grande, depois é diminuida essa lacuna
    lacuna = len(arr) / 2
    round(lacuna)
    #Faz uma inserção com lacuna para o tamanho da lacuna
    #Os primeiros elementos da lacuna a[0...lacuna-1] já estão em ordem
    #lacunadas, continue adicionando mais elemento até o array inteiro estar
    #totalmente ordenado
    while lacuna > 0:

        for i in range(round(lacuna), round(len(arr))):
            #adiciona a[i] aos elementos que já foram ordenados
            #salva a[i] na variavel temp e faz uma brecha na posição i
            temp = arr[i]

            #trocar os elementos anteriores já classificados por lacunas até a localização
            #correta para a[i] for encontrada
            j = i
        while j>=lacuna and arr[j-lacuna] > temp:
            arr[j] = arr[j-lacuna]
            j -= lacuna

        #coloca temp (a variavel original a[i]) em suas posições corretas
        arr[j] = temp
    lacuna /= 2

#Função Main
def main():
    arr = 'entrada10.txt'
    arr = open(arr, 'r')
    li = arr.readlines()
    # Essa parte irá contar quanto tempo foi gasto na execução do algoritmo
    tempinicial = timeit.default_timer()
    arr = shellSort(li)
    tempfinal = timeit.default_timer()
    print('duracao: %f' % (tempfinal - tempinicial))
    print(arr)

if __name__ == "__main__":
    main()



