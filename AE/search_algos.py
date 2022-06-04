'''
Various search algorithms
'''

from typing import List


def load_name(path: str) -> List[str]:
    print(f"Loading Name from `{path}`", end="", flush=True)

    with open(path, encoding="utf8") as text_file:
        names = text_file.read().splitlines()
        print("OK")
        return names


basic_names = load_name("./data/names.txt")
basic_names = load_name("./data/sorted_names.txt")

from random import randint


def random_find(items, srach_val):
    while True:
        random_dex = randint(0, len(items) - 1)
        random_ele = items[random_dex]
        if random_ele == srach_val:
            return random_dex, random_ele


# print("random_find: ", random_find(basic_names, "Fred Astaire"))


def linear_find(items, search_value):
    for index, value in enumerate(items):
        if value == search_value:
            return index, value
    return None


print("linear_find: ", linear_find(basic_names, "Fred Astaire"))


def binary_search(items, search_value):
    left, right = 0, len(items) - 1
    while left <= right:
        mid_idx = (left + right) // 2
        mid_ele = items[mid_idx]
        if mid_ele < search_value:
            left = mid_idx + 1
        elif mid_ele > search_value:
            right = mid_idx - 1
    return None


def binary_search(items, search_value):
    temp = binary_search(items, search_value)
    if temp is None:
        return None
    while items[temp] == search_value and temp >= 0:
        temp -= 1
    return temp + 1
