def cache(func):
    pre_calc={}

    def cache_value(*args, **kwargs):
        value = args[0]

        if value not in pre_calc:
            pre_calc[value] = func(*args, **kwargs)

        return pre_calc[value]

    return cache_value


@cache
def __is_bad_version(n):
    if n > 39:
        return True
    return False

if __name__=="__main__":
    versions = [None] * 50
        
    i = len(versions) // 2
    for x in range(50):
        print(i)
        if versions[i] is None:
            left = __is_bad_version(i + 1)
            versions[i] = left
        if versions[i + 1] is None:
            right = __is_bad_version(i + 2)
            versions[i + 1] = right
            
        print(i)
        if left ^ right:
            print(f"v {i + 1} l {left} r {right}")
            break
            
        if left and right:
            i -= i // 2
            i = max(0, i)
        else:
            i += i // 2
            i = min(48, i)
            
    print(versions)
