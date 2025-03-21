# There is a collection of input strings and a collection of query strings. 
# For each query string, determine how many times it occurs in the list of input strings. 
# Return an array of the results.
#
# Example:
#   stringList=['ab','ab','abc']
#   queries=['ab','abc','bc']
# There are 2 instances of 'ab', 1 of 'abc', and 0 of 'bc'. 
# For each query, add an element to the return array: results=[2,1,0].
import pdb

if __name__=='__main__':
    # my first instinct is to do a double for loop but after
    # a small amount of though I think we can do a hashmap
    stringList=['ab','ab','abc']
    queries=['ab','abc','bc']

    mapping={}

    for s in stringList:
        if s in mapping:
            mapping[s]+=1
        else:
            mapping[s]=1

    results=[]
    for q in queries:
        if q in mapping:
            results.append(mapping[q])
        else:
            results.append(0)

    print(results)
