import time
import math
import copy

class Shuffle:
    def __init__(self, arr):
        self.arr = arr

    def shuffle(self):
        shuffled_arr=[]

        queue=copy.copy(self.arr)
        num=queue.pop(self.__rand_index(len(queue)))
        while len(queue) > 0:
            shuffled_arr.append(num)
            num=queue.pop(self.__rand_index(len(queue)))

        shuffled_arr.append(num)


        return shuffled_arr

    def __rand_index(self, size):
            return math.ceil(time.time() * 1000 % size) - 1


def gen_arr(size):
    arr=[]
    for i in range(size):
        arr.append(i + 1)

    return arr



if __name__=='__main__':
    sol = Shuffle(gen_arr(1000))
    print(sol.arr)
    print(sol.shuffle())
    print(sol.shuffle())
