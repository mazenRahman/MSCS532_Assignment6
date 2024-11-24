import random

def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Randomly choose a pivot
    pivot = random.choice(arr)

    # Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k <= len(low):
        return randomized_select(low, k)
    elif k <= len(low) + len(equal):
        return pivot
    else:
        return randomized_select(high, k - len(low) - len(equal))

# Example Usage
arr3 = [9, 7, 2, 8, 5, 3, 6, 4, 1]
k3 = 5  # Find the 5th smallest element
result3 = randomized_select(arr3, k3)
print(f"Randomized Select - {k3}th smallest element in {arr3}: {result3}")

arr4 = [100, 20, 5, 50, 30, 10, 70, 60]
k4 = 3  # Find the 3rd smallest element
result4 = randomized_select(arr4, k4)
print(f"Randomized Select - {k4}th smallest element in {arr4}: {result4}")
