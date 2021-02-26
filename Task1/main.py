"""
    18. Вернуть в виде списка самую длинную неубывающую подпоследовательность подряд идущих чисел в переданном списке.
    Если можно выделить несколько таких подпоследовательностей одинаковой длины, то вернуть ту,
    сумма элементов которой будет максимальна. Если и сумма элементов совпадает, то вернуть первую
    (от начала списка) такую подпоследовательность.

                      (_ _ _ _ _)
    Example input 1: 9 1 2 2 2 3 1 0 1 1 2 1 7 7
                       _ _ _ _ _  (_ _ _ _ _)
    Example input 2: 9 0 1 1 1 8 7 6 6 7 7 8 2 2
                      (_ _ _ _ _)  _ _ _ _ _
    Example input 3: 9 0 1 1 2 2 1 0 1 1 2 2 1 3
"""


def solve(list_to_solve):
    if not len(list_to_solve):
        return list_to_solve

    current_from = 0
    max_from = 0
    max_to = 0
    max_counter = 0

    max_sum = 0
    current_sum = 0

    for current_to in range(1, len(list_to_solve)):
        if list_to_solve[current_to - 1] <= list_to_solve[current_to]:
            current_sum += list_to_solve[current_to - 1]
            continue
        current_sum += list_to_solve[current_to - 1]
        if current_to - current_from + 1 >= max_counter:
            if current_to - current_from + 1 == max_counter:
                if current_sum <= max_sum:
                    current_sum = 0
                    continue
                current_sum = 0
            max_counter = current_to - current_from + 1
            max_from = current_from
            max_to = current_to
        current_from = current_to
        if current_sum > max_sum:
            max_sum = current_sum
        current_sum = 0
    return list_to_solve.copy() if max_counter == -1 else list_to_solve[max_from:max_to]


print(
    solve(
        [int(item) for item in input().split(' ')]
    )
)
