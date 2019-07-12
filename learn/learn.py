# -*- coding: utf-8 -*-
# import click

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def power(x, n=2):
    return x ** n


def enroll(name, gender, age=6, city='Beijing'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    print(L)
    return L


def calc(base, *numbers):
    sum = 0
    for n in numbers:
        sum += n ** 2
    print(sum + base)
    return sum

def person1(name, age, *kw):
    print(name, age, kw)

def person2(name, age, *, city, job):
    print(name, age, city, job)

def person3(name, age, *args, city, job):
    print(name, age, args, city, job)


# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
# person('Ted', 123, city='Beijing', job='programmer')
num = [2, 3, 4]
calc(1, *num)


# if __name__ == '__main__':
#     hello()
