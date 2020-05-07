# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:42:22 2020

@author: mri08
"""
#Algoritma dan fungsi Untuk Quick Sort (Divide and Conquer Sorting)
def partisi(arr, head, tail):
    i = head - 1
    pivot = arr[tail]
    
    for j in range(head, tail):
        
        #Jika elemen sekarang lebih kecil dari nilai pivot
        if arr[j] < pivot:
            
            #Swap
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[tail] = arr[tail],arr[i+1]
    return i+1

def quickSort(arr, head, tail):
    if head < tail:
        pos_index = partisi(arr, head, tail)
        
        #Pivot akan membagi (divide) list
        quickSort(arr, head, pos_index-1) #Akan Menjadi List yang lebih kecil dari pivot
        quickSort(arr, pos_index + 1, tail) #Akan Menjadi list yang lebih besar dari pivot