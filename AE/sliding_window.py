def find_averages_of_subarrays(k,arr):
    result = []
    window_sum, window_start = 0.0,0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k -1:
            print(window_sum)
            result.append(window_sum/k)
            window_sum -= arr[window_start]
            window_start += 1
    
    return result

# def main():
#     result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
#     print("Averages of subarrays of size K: " + str(result))


# main()

def max_sub_array_of_size_k(k, arr):
    window_sum = 0
    window_start = 0
    max_sum = float("-inf")

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


# def main():
#     print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
#     print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

# main()
def smallest_subarray_with_given_sum(s, arr):
    w_sum = 0.0
    w_start = 0
    w_min = float("inf")

    for w_end in range(len(arr)):
        w_sum += arr[w_end]
        while w_sum >= s:
            w_min = min(w_min,w_end - w_start + 1)
            w_sum -= arr[w_start]
            w_start += 1
    return 0 if w_min == float("inf") else w_min