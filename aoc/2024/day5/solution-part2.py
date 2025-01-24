import copy
import pdb

order_dict,pages_arr={},[]

def parse_input():
    global order_dict, pages_arr
    input="""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    input = [row for row in input.split('\n')]
    split_index = input.index('')

    for item in input[:split_index]:
        pair = item.split('|')

        if pair[0] in order_dict:
            order_dict[pair[0]].append(pair[1])
        else:
            order_dict[pair[0]] = [pair[1]]

    pages_arr = [item.split(',') for item in input[split_index + 1:]]

def bad_pages():
    global order_dict, pages_arr

    tmp=[]
    for page in pages_arr:
        blacklist=[]
        for index in range(len(page) - 1, -1, -1):
            if (page[index] in blacklist):
                tmp.append(page)
                break

            if page[index] in order_dict:
                [blacklist.append(item) for item in order_dict[page[index]]]

    return tmp

def sort_page(page):
    """
    A simple bubble sort
    """
    global order_dict

    done=False
    while not done:
        done=True
        blacklist=[]
        for index in range(len(page) - 1, -1, -1):
            if (page[index] in blacklist):
                done=False
                tmp = page[index]
                page.pop(index)
                page.append(tmp)

            if page[index] in order_dict:
                [blacklist.append(item) for item in order_dict[page[index]]]


def main():
    parse_input()
    pages=bad_pages()

    count=0
    for page in pages:
        sort_page(page)
        count+=int(page[len(page)//2])

    print(count)


if __name__=="__main__":
    main()
