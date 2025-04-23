def cache(func):
    pre_calc = {}

    def cache_value(*args, **kwargs):
        value = args[0]

        if value not in pre_calc:
            pre_calc[value] = func(*args, **kwargs)

        return pre_calc[value]

    return cache_value


@cache
def climb_stairs(level):
    if level <= 0:
        return 0
    elif level == 1 or level == 2:
        return level

    return climb_stairs(level - 2) + climb_stairs(level - 1)


if __name__ == '__main__':
    # two possible ways of stepping up to the top
    # + 1 or + 2
    level = 300
    print(climb_stairs(level))
