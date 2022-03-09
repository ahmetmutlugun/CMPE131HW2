def sort_list(arr: list) -> list:
    n = len(arr)
    i = 0
    while i < n:
        j = 0
        while j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                a = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = a
            j += 1
        i += 1
    return arr
