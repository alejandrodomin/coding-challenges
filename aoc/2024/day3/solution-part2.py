import re

input="""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
valid_matches = re.findall("(mul[(][0-9]{1,3},[0-9]{1,3}[)]|do[(][)]|don't[(][)])", input)

print(valid_matches)

sum=0
enabled=True
for match in valid_matches:
    if match == 'don\'t()':
        enabled = False
    elif match == 'do()':
        enabled = True
    elif enabled:
        nums = re.findall("[0-9]{1,3}", match)

        sum += (int(nums[0]) * int(nums[1]))

print(sum)
