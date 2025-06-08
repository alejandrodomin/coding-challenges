from collections import Set


fn main():
    var s: String = "abcabcbb"

    var backPtr: Int = 0
    var frontPtr: Int = 1

    var longest: Int = 0
    while frontPtr < len(s):
        var setStr: Set[String] = charSet(s[backPtr:frontPtr])
        var length: Int = len(setStr)

        if length == (frontPtr - backPtr) and length > longest:
            longest = length
        else:
            backPtr += 1

        frontPtr += 1

    print("Longest sub string:", longest)


fn charSet(str: String) -> Set[String]:
    var charSet: Set[String] = {}

    for i in range(len(str)):
        charSet.add(str[i])

    return charSet
