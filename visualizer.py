import json
import random

import display

with open('config.json') as config_file:
    data = json.load(config_file)


class Algorithm:
    def __init__(self, name):
        self.name = name
        self.data = random.sample(range(data['height']), data['width'] // 4)

    def update_display(self, swap1=None, swap2=None):
        display.update(self, swap1, swap2)

    def run(self):
        self.algorithm()
        display.wait()


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__('Bubble Sort')

    def algorithm(self):
        end = len(self.data) - 1
        last_swap = end

        for i in range(len(self.data)):
            for j in range(end):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.update_display(self.data[j], self.data[j + 1])
                    last_swap = j

            end = last_swap


class CoctailSort(Algorithm):
    def __init__(self):
        super().__init__('Cocktail Sort')

    def algorithm(self):
        start = 0
        end = len(self.data) - 1
        last_left = 0
        last_right = end
        swapped = True

        while swapped:
            swapped = False

            for i in range(start, end):
                if self.data[i] > self.data[i + 1]:
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]
                    self.update_display(self.data[i], self.data[i - 1])
                    swapped = True
                    last_left = i

            if not swapped:
                break

            swapped = False
            end = last_left

            for i in range(end - 1, start - 1, -1):
                if self.data[i] > self.data[i + 1]:
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]
                    self.update_display(self.data[i], self.data[i + 1])
                    swapped = True
                    last_right = i

            start = last_right


class CombSort(Algorithm):
    def __init__(self):
        super().__init__('Comb Sort')

    def algorithm(self):
        gap = len(self.data)
        swapped = True

        while gap > 1 or swapped:
            gap = int(gap // 1.3)

            if gap == 0:
                gap = 1

            swapped = False

            for i in range(0, len(self.data) - gap):
                if self.data[i] > self.data[i + gap]:
                    self.data[i], self.data[i + gap] = self.data[i + gap], self.data[i]
                    swapped = True
                    self.update_display(self.data[i], self.data[i + gap])


class CycleSort(Algorithm):
    def __init__(self):
        super().__init__('Cycle Sort')

    def algorithm(self):
        for cycle_start in range(len(self.data) - 1):
            item = self.data[cycle_start]
            pos = cycle_start

            for i in range(cycle_start, len(self.data)):
                if item > self.data[i]:
                    pos += 1
                    self.update_display(item, self.data[i])

            if pos == cycle_start:
                continue

            while item == self.data[pos]:
                pos += 1
                self.update_display(item, self.data[pos])

            self.data[pos], item = item, self.data[pos]
            self.update_display(item, self.data[pos])

            while pos != cycle_start:
                pos = cycle_start
                for i in range(cycle_start + 1, len(self.data)):
                    if item > self.data[i]:
                        pos += 1
                        self.update_display(item, self.data[i])

                while item == self.data[pos]:
                    pos += 1
                    self.update_display(item, self.data[pos])

                self.data[pos], item = item, self.data[pos]
                self.update_display(item, self.data[pos])


class GnomeSort(Algorithm):
    def __init__(self):
        super().__init__('Gnome Sort')

    def algorithm(self):
        index = 0

        while index < len(self.data):
            if index == 0:
                index += 1

            if self.data[index] < self.data[index - 1]:
                self.data[index], self.data[index - 1] = self.data[index - 1], self.data[index]
                self.update_display(self.data[index], self.data[index - 1])
                index -= 1

            else:
                index += 1


class HeapSort(Algorithm):
    def __init__(self):
        super().__init__('Heapsort')

    def algorithm(self):
        for i in range((len(self.data) - 1) // 2, -1, -1):
            self.heapify(i, len(self.data))

        size = len(self.data)

        while size > 0:
            self.data[0], self.data[size - 1] = self.data[size - 1], self.data[0]
            size -= 1
            self.heapify(0, size)

    def heapify(self, index, size):
        temp = self.data[index]

        while index < size//2:
            largest_index = 2*index + 1

            if largest_index < size-1 and self.data[largest_index] < self.data[largest_index + 1]:
                largest_index += 1

            if temp >= self.data[largest_index]:
                break

            self.update_display(self.data[index], self.data[largest_index])
            self.data[index] = self.data[largest_index]
            index = largest_index

        self.data[index] = temp


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__('Insertion Sort')

    def algorithm(self):
        for i in range(len(self.data)):
            j = i - 1
            temp = self.data[i]

            while j >= 0 and temp < self.data[j]:
                self.data[j + 1] = self.data[j]
                self.update_display(self.data[j + 1], self.data[j])
                j -= 1

            self.data[j + 1] = temp
            self.update_display(self.data[j], self.data[i])


class MergeSort(Algorithm):
    def __init__(self):
        super().__init__('Merge Sort')

    def algorithm(self, left=-1, right=0):
        if left < right:
            if right == 0 and left == -1:
                left = 0
                right = len(self.data) - 1

            mid = (left + right) // 2
            self.algorithm(left, mid)
            self.algorithm(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        result = [None] * len(self.data)

        for i in range(left, right + 1):
            result[i] = self.data[i]

        i, j, k = left, mid + 1, left

        while i <= mid and j <= right:
            if result[i] <= result[j]:
                self.data[k] = result[i]
                i += 1
                k += 1

            else:
                self.data[k] = result[j]
                j += 1
                k += 1

            self.update_display()

        while i <= mid:
            self.data[k] = result[i]
            i += 1
            k += 1
            self.update_display()

        while j <= right:
            self.data[k] = result[j]
            j += 1
            k += 1
            self.update_display()


class PigeonholeSort(Algorithm):
    def __init__(self):
        super().__init__('Pigeonhole Sort')

    def algorithm(self):
        my_min = min(self.data)
        my_max = max(self.data)

        size = my_max - my_min + 1
        holes = [0] * size

        for x in self.data:
            holes[x - my_min] += 1

        i = 0

        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                self.data[i] = count + my_min
                self.update_display(self.data[i])
                i += 1


class QuickSort(Algorithm):
    def __init__(self):
        super().__init__('Quicksort')

    def algorithm(self, array=None, start=0, end=0):
        if not array:
            array = self.data
            end = len(self.data) - 1

        if start < end:
            p = self.partition(array, start, end)
            self.algorithm(array, start, p - 1)
            self.algorithm(array, p + 1, end)

    def partition(self, array, start, end):
        i = start - 1
        pivot = array[end]

        for j in range(start, end):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
            self.update_display(array[i], array[j])

        array[i + 1], array[end] = array[end], array[i + 1]
        self.update_display(array[i + 1], array[end])

        return i + 1


class RadixSort(Algorithm):
    def __init__(self):
        super().__init__('Radix Sort')

    def algorithm(self):
        maximum = max(self.data)
        exp = 1
        while maximum//exp > 0:
            self.counting_sort(exp)
            exp *= 10

    def counting_sort(self, exp):
        output = [0] * len(self.data)
        count = [0] * 10

        for i in range(0, len(self.data)):
            index = self.data[i] // exp
            count[int(index % 10)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = len(self.data) - 1

        while i >= 0:
            index = self.data[i] / exp
            output[count[int(index % 10)] - 1] = self.data[i]
            count[int(index % 10)] -= 1
            i -= 1

        for i in range(len(self.data)):
            self.data[i] = output[i]
            self.update_display(self.data[i])


class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__('Selection Sort')

    def algorithm(self):
        for i in range(len(self.data)):
            min_idx = i

            for j in range(i + 1, len(self.data)):
                if self.data[min_idx] > self.data[j]:
                    min_idx = j
                    self.update_display(self.data[min_idx], self.data[i])

            self.data[min_idx], self.data[i] = self.data[i], self.data[min_idx]
            self.update_display(self.data[min_idx], self.data[i])


class ShellSort(Algorithm):
    def __init__(self):
        super().__init__('Shellsort')

    def algorithm(self):
        gap = 0

        while gap <= len(self.data)//3:
            gap = gap*3 + 1
            h = gap
            while h > 0:
                for i in range(gap, len(self.data)):
                    temp = self.data[i]
                    j = i

                    while j >= h and self.data[j - h] >= temp:
                        self.update_display(self.data[j], self.data[j - h])
                        self.data[j] = self.data[j - h]
                        j -= h

                    self.data[j] = temp
                    self.update_display(self.data[j], temp)

                h = (h - 1) // 3
