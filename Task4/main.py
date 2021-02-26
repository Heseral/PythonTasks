"""
18.(*) Обработать текст программы на языке C#, заменив все фрагменты вида "переменная = переменная + 1"
(с любым количеством пробелов вокруг символов '=' и '+') на фрагменты "переменная++".
"""
import re


def correct_string(string):
    return re.sub(r'\s*=\s*\S+\s*\+\s*1', '++', string)


def execute(input_name, output_name):
    file_reader = open(input_name)
    file_writer = open(output_name, 'w')
    for line in file_reader:
        file_writer.write(correct_string(line))


execute('input.txt', 'output.txt')
