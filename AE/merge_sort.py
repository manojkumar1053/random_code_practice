def merge_sort(array):
    if len(array) == 1:
        return array

    middle_idx = len(array) // 2
    left_array = array[:middle_idx]
    right_array = array[middle_idx:]
    return merge_sorted_array(merge_sort(left_array), merge_sort(right_array))


def merge_sorted_array(left_half, right_half):
    sorted_array = [None] * (len(left_half) + len(right_half))
    k = i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array[k] = left_half[i]
            i += 1
        else:
            sorted_array[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        sorted_array[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        sorted_array[k] = right_half[j]
        j += 1
        k += 1

    return sorted_array


def mergeSort(array):
    # Write your code here.
    if len(array) <= 1:
        return array
    aux_array = array[:]
    