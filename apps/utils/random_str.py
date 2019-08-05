# -*- coding:utf-8 -*-
# author:h
# datetime:2019-07-31 16:42

import string
from random import choice


def generate_random(random_length, type):
    """"
    :param random_length: number of string to generate
    :param type: 0: just number, 1: number + string, 2: number + string + special character
    :return: random string
    """

    if type == 0:
        random_seed = string.digits
    elif type == 1:
        random_seed = string.digits + string.ascii_letters
    elif type == 2:
        random_seed = string.digits + string.ascii_letters + string.punctuation

    random_str = []

    while len(random_str) < random_length:
        random_str.append(choice(random_seed))

    return ''.join(random_str)


if __name__ == '__main__':
    print(generate_random(4, 0))
