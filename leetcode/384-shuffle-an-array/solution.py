import time
import math
import copy

class Shuffle:
    def __init__(self, arr):
        self.arr = arr

    def shuffle(self):
        shuffled_arr=[]

        queue=copy.copy(self.arr)
        while len(queue) > 0:
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
    sol = Shuffle(gen_arr(10))
    print(sol.arr)
    for i in range(5):
        # suffering from success, algorithm runs so fast that 
        # the time.time() isn't different enough unless I manually add a pause
        time.sleep(1)
        print(sol.shuffle())
