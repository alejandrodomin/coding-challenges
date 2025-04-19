input="XLIX"

rom_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

total, last = 0, 0
for letter in input[::-1]:
    value = rom_map[letter] 
     
    if value >= last:
        total += value
        last = value
    else:
        total -= value
    
    
print(total)