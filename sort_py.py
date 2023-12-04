import time
import pandas as pd
import pathlib
from pathlib import Path

def insertion_sort(nums):  
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert

def sorting_file(count_files):
    sort_length_array = []
    sort_time_array = []
    i = 1
    while i <= count_files:
        with open(Path(f"LR1/sort_arr/sort_arr{i}.txt"), 'r') as file:
            array = [int(row.strip()) for row in file]
            sort_length_array.append(len(array))
            start = time.time()
            insertion_sort(array)
            sort_time_array.append(time.time() - start)
            print(sort_length_array)
            print(sort_time_array)
        with open(f"LR1/sort_arr_result/sort_arr_result{i}.txt", "w") as file:
                file.writelines("%s\n" % result for result in array)
        i += 1
    record_in_excel(sort_length_array,sort_time_array)

def record_in_excel(sort_length_array,sort_time_array):
    df = pd.DataFrame({
        'Array_length': [sort_length_array[0], sort_length_array[1], sort_length_array[2], sort_length_array[3], sort_length_array[4]],
        'Sorting_time': [sort_time_array[0], sort_time_array[1], sort_time_array[2], sort_time_array[3],sort_time_array[4]]})
    df.to_excel('LR1/sort_results.xlsx', index=False)

sorting_file(5)
