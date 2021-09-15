import json

import pygame

import algorithms
import display

with open('config.json', 'r') as config_file:
    data = json.load(config_file)

pygame.init()

sorting_algorithms = {'bubble sort': algorithms.BubbleSort,
                      'coctail sort': algorithms.CoctailSort,
                      'comb sort': algorithms.CombSort,
                      'cycle sort': algorithms.CycleSort,
                      'gnome sort': algorithms.GnomeSort,
                      'heap sort': algorithms.HeapSort,
                      'insertion sort': algorithms.InsertionSort,
                      'merge sort': algorithms.MergeSort,
                      'pigeonhole sort': algorithms.PigeonholeSort,
                      'quick sort': algorithms.QuickSort,
                      'radix sort': algorithms.RadixSort,
                      'selection sort': algorithms.SelectionSort,
                      'shell sort': algorithms.ShellSort
                      }


def main():
    run = True
    user_text = None

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            user_text = display.input_box.handle_event(event)

        if user_text is not None:
            user_text = user_text.lower().strip()

            if user_text == 'exit':
                break

            try:
                algorithm = sorting_algorithms[user_text]()
                algorithm.run()
            except KeyError:
                display.display_message('Invalid name')
                display.wait()

            user_text = None
            display.input_box.text = ''

        display.input_box.update()

        display.WIN.fill((30, 30, 30))
        display.input_box.draw(display.WIN)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
