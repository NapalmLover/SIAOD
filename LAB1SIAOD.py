import random
import time


def random_matrix(m = 1000, n = 1000, min_limit = -250, max_limit = 1016):
    return [[random.randint(min_limit, max_limit) for _ in range(n)] for _ in range(m)]
amogus = random_matrix()


def selection_sort(arr):
    for i, e in enumerate(arr):
        mn = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[mn] = arr[mn], e
    return arr



def quick_sort(arr, fst=0, lst=None):
    if lst == None:
        lst = len(arr) - 1

    if fst >= lst:
        return

    i, j = fst, lst
    pivot = arr[(lst + fst) // 2]

    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1

    quick_sort(arr, fst, j)
    quick_sort(arr, i, lst)




amogus = random_matrix()
start = time.time()
sel = selection_sort(amogus)
print("Время выполнения ВС: ", (time.time() - start)*1000)

start = time.time()
quk = quick_sort(amogus)
print("Время выполнения БС: ", (time.time() - start)*1000)

start = time.time()
typ = amogus.sort()
print("Время выполнения СП: ", (time.time() - start)*1000)
