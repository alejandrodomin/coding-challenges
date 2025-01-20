import re

input="""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
valid_matches = re.findall("mul[(][0-9]{1,3},[0-9]{1,3}[)]", input)

sum=0
for match in valid_matches:
    nums = re.findall("[0-9]{1,3}", match)

    sum += (int(nums[0]) * int(nums[1]))

print(sum)
