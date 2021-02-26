"""
    18. (*) Будем называть «дружественными» элементами для двумерного массива такие элементы,
    которые соединяются с данным элементом одной из сторон и имеют одно и то же значение,
    а также все дружественные элементы для дружественных элементов данного элемента.
    Составить для переданного двумерного массива новый массив, в котором каждый элемент будет
    содержать информацию о количестве дружественных элементов для соответствующего элемента в переданном массиве.
"""
import copy
import sys


def solve_all(input_list):
    output_list = []
    for current_list in input_list:
        output_list.append(
            [0 for _ in range(len(current_list))]
        )
    visited_list = copy.deepcopy(output_list)
    for row in range(len(output_list)):
        for col in range(len(output_list[row])):
            visited_list[row][col] = 1
            output_list[row][col] = solve(input_list, row, col, copy.deepcopy(visited_list))
            visited_list[row][col] = 0
    return output_list


def solve(input_list, row, col, visited_list):
    result = 0
    if row > 0 \
            and input_list[row][col] == input_list[row - 1][col] \
            and not visited_list[row - 1][col]:
        visited_list[row - 1][col] = 1
        result += solve(input_list, row - 1, col, visited_list) + 1
    if col > 0 \
            and input_list[row][col] == input_list[row][col - 1] \
            and not visited_list[row][col - 1]:
        visited_list[row][col - 1] = 1
        result += solve(input_list, row, col - 1, visited_list) + 1
    if row < len(input_list) - 1 \
            and input_list[row][col] == input_list[row + 1][col] \
            and not visited_list[row + 1][col]:
        visited_list[row + 1][col] = 1
        result += solve(input_list, row + 1, col, visited_list) + 1
    if col < len(input_list[row]) - 1 \
            and input_list[row][col] == input_list[row][col + 1] \
            and not visited_list[row][col + 1]:
        visited_list[row][col + 1] = 1
        result += solve(input_list, row, col + 1, visited_list) + 1
    return result


def print_matrix(matrix):
    for current_list in matrix:
        for item in current_list:
            sys.stdout.write(str(item))
            sys.stdout.write(' ')
        print()


print_matrix(
    solve_all(
        [
            [1, 1, 2, 1],
            [1, 3, 2, 4],
            [1, 1, 1, 1],
            [1, 3, 4, 5]
        ]
    )
)
