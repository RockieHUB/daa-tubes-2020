# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:44:20 2020

@author: mri08
"""

import random
import time
from QS import *
from SS import *

n = 500
#Isi Array dengan angka random
arr = random.sample(range(1,999),n)

#Duplicate array untuk setiap metode Sorting
arr1 = arr.copy()
arr2 = arr.copy()

print("Randomized Array")
print(arr)
print("")

#Quick Sort

print("Randomized Array for Quick Sort     : ")
print(arr1)
last_index = len(arr1) - 1

#Calculate Time for main Quick Sort Function
start_time = time.time()
quickSort(arr1, 0, last_index)
print("Updated Array with Quick Sort       : ")

print(arr1)
print("--- %s seconds ---" % (time.time() - start_time))
print("")

#Selection Sort
print("Randomized Array for Selection Sort : ")
print(arr2)

#Calculate Time for main Quick Sort Function
start_time = time.time()
selectionSort(arr2)

print("Updated Array with Selection Sort   : ")
print(arr2)
print("--- %s seconds ---" % (time.time() - start_time))