"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import time
import timeit


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

def experiment(n):
    for i in range(n):
        total1 = 0
        total2 = 0
        total3 = 0

        numberOfElements = 1000
        randomList = create_random_list(numberOfElements, 10000)

        start = timeit.default_timer()
        bubble_sort(randomList)
        total1 += timeit.default_timer() - start
        if n>1:
            print("Bubble sort -- listLength: ", numberOfElements, " time: ", total1/n, "sec")
        else:
            print("Bubble sort -- listLength: ", numberOfElements, " time: ", total1, "sec")

        start = timeit.default_timer()
        selection_sort(randomList)
        total2 += timeit.default_timer() - start
        if n>1:
            print("Selection sort -- listLength: ", numberOfElements, " time: ", total2/n, "sec")
        else:
            print("Selection sort -- listLength: ", numberOfElements, " time: ", total2, "sec")

        start = timeit.default_timer()
        insertion_sort(randomList)
        total3 += timeit.default_timer() - start
        if n>1:
            print("Insertion sort -- listLength: ", numberOfElements, " time: ", total2/n, "sec")
        else:
            print("Insertion sort -- listLength: ", numberOfElements, " time: ", total2, "sec")

def main():
    experiment(1);
    experiment(100);

main()