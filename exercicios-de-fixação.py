def exercise(array1, array2):
    interactions = 0
    for n in array1:
        start = 0
        end = len(array2)
        inter = 0
        while start < end:
            mid = (start + end) // 2
            start = mid + 1
            interactions += 1
            inter += 1
            print(interactions)

    return len(array1) * interactions


print(exercise([1, 2, 3, 4], [1, 2, 3, 4]))
