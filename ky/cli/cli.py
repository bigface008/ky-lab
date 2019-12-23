import pandas as pd
import numpy as np
import re
import random
import time

SIMPLE_HASH = 0
COMPLEX_HASH = 1

class LinearHashMap(object):
    def __init__(self, size, hashFunc):
        self.basic_size = size
        self._list = []
        self._hash = hashFunc
        for i in range(size):
            self._list.append([])

    def Set(self, key, value):
        calc_key = self._hash(key, self.basic_size)
        tmp_list = self._list[calc_key]
        for i in range(len(tmp_list)):
            if tmp_list[i][0] == key:
                tmp_val = tmp_list[i][1]
                if tmp_val == value:
                    # print('Same value.')
                    return value
                tmp_list[i][1] = value
                # self._logSet(key, value, i, calc_key)
                return (key, tmp_val)
            else:
                continue
        tmp_list.append([key, value])
        # self._logSet(key, value, 0, calc_key)
        if len(tmp_list) > self.basic_size / 2:
            self._expand()
        return value

    def Get(self, key):
        calc_key = self._hash(key, self.basic_size)
        tmp_list = self._list[calc_key]
        for i in range(len(tmp_list)):
            if tmp_list[i][0] == key:
                # self._logGet(key, tmp_list[i][1], i, calc_key)
                return tmp_list[i][1]
            elif tmp_list[i] == []:
                # print('Find failed of key %d', key)
                return
            else:
                continue
        # print('Find failed of key %d', key)
        return None

    def Delete(self, key):
        calc_key = self._hash(key, self.basic_size)
        tmp_list = self._list[calc_key]
        for i in range(len(tmp_list)):
            if tmp_list[i][0] == key:
                # self._logDelete(key, tmp_list[i][1], i, calc_key)
                tmp_list.pop(i)
                return
            elif tmp_list[i] == []:
                # print('Find failed of key %d', key)
                return
            else:
                continue
        # print('Find failed of key %d', key)
        return
    
    def _expand(self):
        # print('Trigger expandation.')
        new_list = []
        for i in range(self.basic_size * 2):
            new_list.append([])
        for i in range(self.basic_size):
            for j in range(len(self._list[i])):
                key = self._list[i][j][0]
                value = self._list[i][j][1]
                calc_key = self._hash(key, self.basic_size * 2)
                tmp_list = new_list[calc_key]
                tmp_list.append([key, value])
        self._list = new_list
        self.basic_size *= 2
        # print('Finish expandation.')
        return

    def logContent(self):
        print(self._list)

    def _logSet(self, key, value, i, calc_key):
        print('Insert key %s value %s at %d of %d in linear' % (key, value, i, calc_key))

    def _logGet(self, key, value, i, calc_key):
        print('Find key %s value %s at %d of %d in linear' % (key, value, i, calc_key))

    def _logDelete(self, key, value, i, calc_key):
        print('Delete key %s value %s at %d of %d in linear' % (key, value, i, calc_key))


class CuckooHashMap(object):
    def __init__(self, size):
        self.map1 = LinearHashMap(size, h1_hash)
        self.map2 = LinearHashMap(size, h2_hash)

    def Set(self, key, value):
        test = self.map1.Set(key, value)
        prev_map = 1
        val_list = []
        while type(test) == tuple:
            prev_val = test[1]
            for i in range(len(val_list)):
                if val_list[i] == prev_val:
                    self._expand()
            val_list.append(prev_val)
            if prev_map == 1:
                test = self.map2.Set(key, prev_val)
                prev_map = 2
            else:
                test = self.map1.Set(key, prev_val)
                prev_map = 1
        # print('Set succeed.')
        return value

    def Get(self, key):
        test1 = self.map1.Get(key)
        if test1 == None:
            test2 = self.map2.Get(key)
            if test2 == None:
                return None
            else:
                return test2
        else:
            return test1

    def Delete(self, key):
        # print('Expand')
        self.map1.Delete(key)
        self.map2.Delete(key)

    def _expand(self):
        self.map1._expand()
        self.map2._expand()

    def logContent(self):
        self.map1.logContent()
        self.map2.logContent()


def h1_hash(key, size):
    return key % size


def h2_hash(key, size):
    return (key // size) % size

def test_0(test_map):
    start_time = time.time()
    for i in range(10000):
        if i == 999:
            end_time = time.time()
        test_map.Set(random.randint(0, 10000), i)
    print(end_time - start_time)

# def test_1(test_map):


def main():
    # map1 = LinearHashMap(8, h1_hash)
    map1 = CuckooHashMap(8)
    # map1.Set(5, 12)
    # print(map1.Get(5))
    # map1.Set(12, 7)
    # map1.Set(22, 9)
    # map1.Set(11, 99)
    # print(map1.Get(22))
    # map1.Set(22, 1)
    # print(map1.Get(22))
    # map1.Delete(22)
    # print(map1.Get(22))
    # map1.logContent()
    # commands = []
    # with open(r'D:\workspace\python\ky-lab\ky\data\large.in', 'r') as f:
    with open(r'D:\workspace\python\ky-lab\ky\data\small.in', 'r') as f:
        for i in f.readlines():
            command = i.rstrip().split()
            # print(command)
            if command[0] == 'Set':
                map1.Set(int(command[1]), int(command[2]))
            elif command[0] == 'Get':
                get_content = map1.Get(int(command[1]))
                print(get_content if get_content != None else 'null')
            else:
                map1.Delete(int(command[1]))
            # commands.append(i.rstrip().split())


if __name__ == "__main__":
    # main()
    map1 = LinearHashMap(8, h1_hash)
    map2 = CuckooHashMap(8)
    test_0(map1)
    test_0(map2)
    