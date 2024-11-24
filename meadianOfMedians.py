def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Divide the array into sublists of 5
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Recursively find the median of medians
    pivot = deterministic_select(medians, len(medians) // 2 + 1)

    # Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k <= len(low):
        return deterministic_select(low, k)
    elif k <= len(low) + len(equal):
        return pivot
    else:
        return deterministic_select(high, k - len(low) - len(equal))

# Example Usage
arr1 = [12, 3, 5, 7, 19, 26, 4, 2]
k1 = 4  # Find the 4th smallest element
result1 = deterministic_select(arr1, k1)
print(f"Deterministic Select - {k1}th smallest element in {arr1}: {result1}")

arr2 = [10, 20, 30, 40, 50, 60, 70, 80]
k2 = 6  # Find the 6th smallest element
result2 = deterministic_select(arr2, k2)
print(f"Deterministic Select - {k2}th smallest element in {arr2}: {result2}")
