import random
import time
import copy


def insertion_sort(data):
    data = copy.copy(data)
    N = len(data)

    for i in range(1, N):
        temp = data[i]

        j = i - 1
        while j >= 0 and temp < data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = temp

    return data


def shell_sort(data):
    data = copy.copy(data)

    N = len(data)
    h = N // 2

    while h >= 1:
        for i in range(h, N):
            temp = data[i]
            j = i

            while j >= h and temp < data[j - h]:
                data[j] = data[j - h]
                j -= h

            data[j] = temp

        h = h // 2

    return data


def main():
    unsorted_list = [int(random.random() * 100) for i in range(10000)]

    t_start_1 = time.perf_counter()

    sorted_list_2 = shell_sort(unsorted_list)

    t_stop_1 = time.perf_counter()

    t_start_2 = time.perf_counter()

    sorted_list_2 = insertion_sort(unsorted_list)

    t_stop_2 = time.perf_counter()

    print("Czas obliczeń (shell, insertion):", "{:.7f}, {:.7f}".format(t_stop_1 - t_start_1, t_stop_2 - t_start_2))


main()
