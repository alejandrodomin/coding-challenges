def search(nums_arr, target):
    index = len(nums_arr) // 2
    
    if index == 0:
        print(f"Target {target} not found")
        exit(1)

    if nums_arr[index] == target:
        return index
    elif nums_arr[index] > target:
        return search(nums_arr[:index], target)
    elif nums_arr[index] < target:
        return index + search(nums_arr[index:], target)
    

if __name__=='__main__':
    print(search([-1,0,3,5,9,12], 4))
