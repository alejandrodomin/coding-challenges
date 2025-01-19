import copy
import queue

bin_str='101100'
n_bin=bin_str.count('1')
arr = ['?110?1', '111???']
possibilities={}

def gen_possibilities(string):
    global possibilities

    possible=queue.Queue()
    possible.put(list(string))

    while possible.qsize() > 0:

        tmp = possible.get()

        if '?' in tmp:
            for index in range(len(tmp)):
                if tmp[index] == '?':
                    zero = copy.copy(tmp)
                    zero[index] = '0'

                    possible.put(zero)

                    one = copy.copy(tmp)
                    one[index] = '1'

                    possible.put(one)
        else:
            possibility = ''.join(tmp)
            
            if possibility.count('1') <= n_bin and possibility not in possibilities[string]:
                possibilities[string].append(possibility)

solutions=[]
for test_case in arr:
    possibilities[test_case] = []
    gen_possibilities(test_case)

    possible=True
    for possibility in possibilities[test_case]:
        for index in range(len(possibility)):
            if possibility[:index].count('1') > bin_str[:index].count('1'):
                possible=False
                continue

    if possible:
        solutions.append("YES")
    else:
        solutions.append("NO")


print(possibilities)
print(solutions)

