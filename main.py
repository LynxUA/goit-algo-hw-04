import matplotlib.pyplot as plt
import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def run_experiment():
    sizes = [100, 1000, 10000, 100000]
    results = {
        'merge_sort': [],
        'insertion_sort': [],
        'timsort': []
    }

    print("Please wait, the calculation will take a while")
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]

        print(f'Calculating merge sort for {size}')
        merge_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
        results['merge_sort'].append(merge_time)
        print(f'It took {round(merge_time, 2)}')
        print(f'Calculating insertion sort for {size} seconds')
        insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
        results['insertion_sort'].append(insertion_time)
        print(f'It took {round(insertion_time, 2)} seconds')
        print(f'Calculating timsort for {size}')
        timsort_time = timeit.timeit(lambda: sorted(arr.copy()), number=1)
        results['timsort'].append(timsort_time)
        print(f'It took {round(timsort_time, 2)} seconds')

    return sizes, results

def plot_results(sizes, results):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, results['merge_sort'], label='Merge Sort')
    plt.plot(sizes, results['insertion_sort'], label='Insertion Sort')
    plt.plot(sizes, results['timsort'], label='Timsort')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

sizes, results = run_experiment()
plot_results(sizes, results)
