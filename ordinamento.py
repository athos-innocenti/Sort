import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

sys.setrecursionlimit(100000)


def random_list(n):
    ls = list(range(n))
    random.shuffle(ls)
    return ls


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


def insertion_sort_time(a):
    start = timer()
    insertion_sort(a)
    end = timer()
    time_i = end - start
    print "Tempo di esecuzione InsertionSort:", time_i
    return time_i


def quicksort_time(b, n):
    start = timer()
    quicksort(b, 0, n - 1)
    end = timer()
    time_q = end - start
    print "Tempo di esecuzione Quicksort:", time_q
    return time_q


def average(values):
    values_sum = 0
    for i in range(len(values)):
        values_sum += values[i]
    avg = values_sum / len(values)
    return avg


def main():
    tries = 20
    step = 100
    max_size = 4001
    size = np.arange(0, max_size, step)

    time_insertion = []
    time_quick = []
    for dim in range(0, max_size, step):
        print "Dimensione:", dim
        tries_insertion = []
        tries_quick = []
        for j in range(0, tries):
            a = random_list(dim)  # CASO MEDIO
            b = a[:]
            tries_insertion.append(insertion_sort_time(a))
            tries_quick.append(quicksort_time(b, dim))
        time_insertion.append(average(tries_insertion))
        time_quick.append(average(tries_quick))
    plt.plot(size, time_insertion)
    plt.xlabel('Dimensione array')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Caso medio di Insertion sort')
    plt.show()
    plt.plot(size, time_quick)
    plt.xlabel('Dimensione array')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Caso medio di Quicksort')
    plt.show()
    plt.plot(size, time_insertion)
    plt.plot(size, time_quick)
    plt.xlabel('Dimensione array')
    plt.ylabel('Tempo di esecuzione')
    plt.legend(['Insertion sort', 'Quicksort'])
    plt.title('Confronto nel caso medio')
    plt.show()

    time_insertion = []
    time_quick = []
    for dim in range(0, max_size, step):
        print "Dimensione:", dim
        tries_insertion = []
        tries_quick = []
        a = list(range(dim))  # CASO MIGLIORE INSERTION SORT
        b = a[:]
        for j in range(0, tries):
            tries_insertion.append(insertion_sort_time(a))
            tries_quick.append(quicksort_time(b, dim))
        time_insertion.append(average(tries_insertion))
        time_quick.append(average(tries_quick))
    plt.plot(size, time_insertion)
    plt.xlabel('Dimensione array')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Caso migliore di Insertion sort')
    plt.show()
    plt.plot(size, time_quick)
    plt.xlabel('Dimensione array')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Quicksort nel caso migliore di Insertion sort')
    plt.show()
    plt.plot(size, time_insertion)
    plt.plot(size, time_quick)
    plt.xlabel('Dimensione array')
    plt.ylabel('Tempo di esecuzione')
    plt.legend(['Insertion sort', 'Quicksort'])
    plt.title('Confronto nel caso migliore di Insertion-Sort')
    plt.show()

    time_insertion = []
    time_quick = []
    for dim in range(0, max_size, step):
        print "Dimensione:", dim
        tries_insertion = []
        tries_quick = []
        a = list(reversed(list(range(dim))))  # CASO PEGGIORE INSERTION SORT
        b = a[:]
        for j in range(0, tries):
            tries_insertion.append(insertion_sort_time(a))
            tries_quick.append(quicksort_time(b, dim))
        time_insertion.append(average(tries_insertion))
        time_quick.append(average(tries_quick))
    plt.plot(size, time_insertion)
    plt.xlabel('Dimensione array')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Caso peggiore di Insertion sort')
    plt.show()
    plt.plot(size, time_quick)
    plt.xlabel('Dimensione array')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Quicksort nel caso peggiore di Insertion sort')
    plt.show()
    plt.plot(size, time_insertion)
    plt.plot(size, time_quick)
    plt.xlabel('Dimensione array')
    plt.ylabel('Tempo di esecuzione')
    plt.legend(['Insertion sort', 'Quicksort'])
    plt.title('Confronto nel caso peggiore di Insertion-Sort')
    plt.show()


if __name__ == '__main__':
    main()
