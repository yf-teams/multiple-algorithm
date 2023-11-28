import copy
import os
import time

def binary_search(arr):
    arr.sort(key=lambda x: x[0])
    l = 0
    r = len(arr) - 1

    try:
        # 將使用者輸入的值轉換為整數
        value = int(input("輸入要尋找的值: "))
    except ValueError:
        print("請輸入有效的整數值。")
        return

    while l <= r:
        mid = l + (r - l) // 2
        mid_value = arr[mid][0]

        if mid_value == value:
            print(f"在排序後索引 {mid} 找到值 {value}，在原始數組中的位置是 {arr[mid][1]}")
            return
        elif mid_value < value:
            l = mid + 1
        else:
            r = mid - 1
    print(f"找不到值 {value}")


def sequential_search(arr, value, speed):
    found = False
    for i in range(len(arr)):
        if arr[i][0] == value:
            found = True
            time.sleep(speed)
            clear_screen()
            print(f"在索引 {i} 找到值 {value}")
            break

    if not found:
        time.sleep(speed)
        clear_screen()
        print(f"找不到值 {value}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # 清除屏幕的命令

def bubble_sort(arr, speed):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                time.sleep(speed)
                clear_screen()
                print(f"比較 {arr[j][0]} 和 {arr[j + 1][0]}: 交換位置")
                print("當前數組狀態:")
                for x in arr:
                    print(f"{x[0]:2}", end=" ")
                print()

def selection_sort(arr, speed):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        time.sleep(speed)
        clear_screen()
        print(f"比較 {arr[i][0]} 和 {arr[min_idx][0]}: 交換位置")
        print("當前數組狀態:")
        for x in arr:
            print(f"{x[0]:2}", end=" ")
        print()

def insertion_sort(arr, speed):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[0] < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        time.sleep(speed)
        clear_screen()
        print(f"插入 {key[0]} 到適當位置")
        print("當前數組狀態:")
        for x in arr:
            print(f"{x[0]:2}", end=" ")
        print()

def apply_sorting_algorithm(arr, algorithm, speed):
    sorted_arr = copy.deepcopy(arr)
    algorithm(sorted_arr, speed)
    print(f"使用 {algorithm.__name__} 排序後:")
    print(" ".join(f"{x[0]:2}" for x in sorted_arr))

# 測試
arr = [64, 34, 25, 12, 22, 11, 90, 45, 77, 33, 55, 18]

for i in range(len(arr)):
    arr[i] = [arr[i], i]


print("原始數組:")
print(" ".join(f"{x[0]:2}" for x in arr))

while True:
    print("主選單:")
    print("1. 排序")
    print("2. 循序搜尋")
    print("3. 二分搜尋")
    print("0. 結束")

    main_choice = input("請輸入主選單中的選擇: ")

    if main_choice == '0':
        break
    elif main_choice == '1':
        sorting_choice = input("排序選單: 1. 冒泡排序, 2. 選擇排序, 3. 插入排序, 0. 返回主選單: ")
        if sorting_choice == '0':
            continue
        speed = float(input("設定排序速度 (輸入等待時間，例如0.1表示0.1秒): "))
        algorithm = None
        if sorting_choice == '1':
            algorithm = bubble_sort
        elif sorting_choice == '2':
            algorithm = selection_sort
        elif sorting_choice == '3':
            algorithm = insertion_sort
        else:
            print("請輸入有效的排序選擇 (1, 2, 3, 0)。")
            continue
        apply_sorting_algorithm(arr, algorithm, speed)
    elif main_choice == '2':
        target = int(input("輸入要尋找的值: "))
        speed = float(input("設定搜索速度 (輸入等待時間，例如0.1表示0.1秒): "))
        sequential_search(arr, target, speed)
    elif main_choice == '3':
      binary_search(arr)
    else:
        print("請輸入有效的主選單選擇 (1, 2, 3, 0)。")
