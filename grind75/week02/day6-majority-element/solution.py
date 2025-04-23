# first instincts is to create either a hashmap or an array and use the number
# in the nums array as an index and then just use a counter and from there we
# can grab the index with the biggest number thus the majority number.
# Prompt is asking for O(1) space complexity so lets see if we can do that.

if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]

    vote, count = 0, 0

    for num in nums:
        if num != vote and count == 0:
            vote = num

        if vote == num:
            count += 1
        else:
            count -= 1

    print(vote)
