#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import timeit

# Créditos para:
# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html

sys.setrecursionlimit(1000000)

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def main():
    #Arquivo para teste
    arquivo = open('entrada100000.txt', 'r')
    dados = arquivo.read()
    elementos = [int (i) for i in dados.split()]
    print('\tTamanho: ',len(elementos))
    #print('\nSEM ORDENAR -> ', elementos)
    inicio = 0
    fim = len(elementos)-1
    #Essa parte irá contar quanto tempo foi gasto na execução do algoritmo
    tempinicial = timeit.default_timer()
    quickSort(elementos)
    tempfinal = timeit.default_timer()
    print('\nDEPOIS DE ORDENAR -> ', elementos)
    print('\n\t\tDuracao: %f' % (tempfinal - tempinicial))


if __name__ == "__main__":
    main()