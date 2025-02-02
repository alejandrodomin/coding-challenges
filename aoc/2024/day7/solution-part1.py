import heapq
import pdb

formula_dict={}

def parse_input():
    global formula_dict
    input="""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    for line in input.split("\n"):
        formula = line.split(":")
        formula_dict[int(formula[0])] = [int(num) for num in filter(None, formula[1].split(" "))]

    print(formula_dict)


def main():
    global formula_dict
    parse_input()

    count=0
    for formula in formula_dict:
        calc_queue=[]
        heapq.heappush(calc_queue, formula_dict[formula][0])

        pdb.set_trace()

        for number in formula_dict[formula][1:]:
            tmp = heapq.heappop(calc_queue)

            if tmp == formula:
                count+=formula
            elif tmp > formula:
                break
            else:
                # because we are iterating over the dicitonary and not the pq we need to do these checks first

                heapq.heappush(calc_queue, number + tmp)
                heapq.heappush(calc_queue, number * tmp)

    print(count)









if __name__=="__main__":
    main()
