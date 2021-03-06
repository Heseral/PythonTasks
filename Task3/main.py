"""
18. Прайс-лист содержит следующую информацию о планшетах: название модели, объем памяти,
рейтинг модели среди пользователей (цифра от 1 до 5), стоимость.
У вас есть N денег, вам необходимо купить самый хороший планшет, на который вам хватит денег.
Для вас приоритетным является объем памяти, в случае одинакового объема – рейтинг модели.
Если подходящих моделей будет несколько, вы выберете Samsung или Asus (присутствует в названии модели),
а затем все остальные. Если по этим критериям вам подходят несколько моделей – выбирайте любой.

Входные данные соответствуют предыдущей задачи, однако теперь вам надо купить K самых дешевых планшетов
с объемом памяти не ниже M и рейтингом не ниже R (призы победителям олимпиады).
Какие планшет вы выберете и сколько денег вы потратите?
"""
import random

from tablet import Tablet


def fill_input_randomly(file_name, amount):
    file = open(file_name, 'w')
    for i in range(amount - 1):
        file.write(
            Tablet(
                random.choice(['Samsung', 'Xiaomi', 'Asus', 'Lenovo', 'Huawei']),
                random.randrange(1024, 16384, 512),
                random.randint(1, 5),
                random.randint(1000, 20000)
            ).as_string() + '\n'
        )


def read_tablets_from_file(file_name):
    file = open(file_name)
    result = []
    for line in file:
        result.append(tablet_from_string(line))
    return result


def tablet_from_string(string):
    return tablet_from_args(string.split(' '))


def tablet_from_args(args):
    return Tablet(args[0], int(args[1]), int(args[2]), int(args[3]))


def find_tablets(input_tablets, amount, min_ram, min_rating):
    output_tablets = []
    input_tablets.sort(key=lambda tablet_to_sort: tablet_to_sort.price)
    amount_bought = 0
    for tablet_input in input_tablets:
        if tablet_input.ram >= min_ram and tablet_input.rating >= min_rating:
            output_tablets.append(tablet_input)
            amount_bought += 1
        if amount_bought >= amount:
            break
    return output_tablets


def fill_output_with_tablets(file_name, tablets):
    file = open(file_name, 'w')
    for tablet in tablets:
        file.write(tablet.as_string() + '\n')


def solve():
    input_name = 'input.txt'
    output_name = 'output.txt'
    amount_input = 100
    amount_output = 10
    min_ram = 2048
    min_rating = 3
    fill_input_randomly(input_name, amount_input)

    output_tablets = find_tablets(
            read_tablets_from_file(input_name),
            amount_output,
            min_ram,
            min_rating
    )
    total_price = 0
    for tablet in output_tablets:
        total_price += tablet.price

    print(f'Total price is {total_price}')
    fill_output_with_tablets(output_name, output_tablets)


solve()
