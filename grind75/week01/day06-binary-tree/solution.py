import numpy

def invert_tree(tree):
    done = False
    level=0
    window_size=1
    ptr=0

    inverted_tree=[]

    while not done:
        section=tree[ptr:ptr+window_size]
        inverted_tree.extend(section[::-1])

        ptr+=window_size
        level+=1

        window_size = numpy.power(2, level)
        if ptr + window_size > len(tree):
            done=True
            window_size = len(tree) - ptr

    return inverted_tree
    

if __name__=='__main__':
    tree=[4,2,7,1,3,6,9]
    print(invert_tree(tree))
