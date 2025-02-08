def two_sum_ai(nums, target):
    """ 
    solution below was created by AI
    else statement and the dictionary makes no sense to me
    """
    num_dict = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in num_dict:
            print(f"Indices: {num_dict[complement]}, {i}")
        else:
            num_dict[nums[i]] = i

def two_sum(nums, target):
    """ 
    My solution is a bit slower to the AIs due to the constant calls to nums.index
    """
    for i in range(len(nums)):
        wrk_num = target- nums[i]

        if wrk_num in nums and nums.index(complement) != i:
            print(f"Found solution at indeces: {nums.index(wrk_num)},{i}")
            break

input_nums=[150,24,79,50,88,345,3]
target=200
two_sum(input_nums, target)