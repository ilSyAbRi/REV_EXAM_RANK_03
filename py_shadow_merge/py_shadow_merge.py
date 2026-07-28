def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    list3 = list1 + list2
    list3.sort()

    return list3

print(shadow_merge([1,3,5], [2,4,6]))
