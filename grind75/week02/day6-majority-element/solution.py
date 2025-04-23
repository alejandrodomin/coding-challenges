# first instincts is to create either a hashmap or an array and use the number
# in the nums array as an index and then just use a counter and from there we
# can grab the index with the biggest number thus the majority number.
# Prompt is asking for O(1) space complexity so lets see if we can do that.

if __name__ == '__main__':
    nums = [3, 3, 4]

    n_map = {}
    for num in nums:
        if num not in n_map:
            n_map[num] = 0

        n_map[num] += 1

    m_value,  m_count = 0, 0
    for key in n_map:
        if n_map[key] > m_count:
            m_value = key
            m_count = n_map[key]

    print(m_value)
