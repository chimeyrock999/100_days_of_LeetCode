from typing import List

array = [64, 34, 25, 12, 22, 11, 90, 5]


def quick_sort(array: List[int], left: int, right: int):
    if left == right:
        return

    i = left
    j = right
    pivot = array[(left+right)//2]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    quick_sort(array, left, j)
    quick_sort(array, i, right)

print(array)
quick_sort(array, 0, len(array)-1)
print(array)