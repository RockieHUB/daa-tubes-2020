# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:43:42 2020

@author: mri08
"""
#Algoritma untuk Selection Sort (Brute Force Sorting)
def selectionSort(arr):
    for i in range(len(arr)):
        #Cari index dengan nilai minimum
        min = i
        
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        #Swap
        arr[i], arr[min] = arr[min], arr[i]