def is_anagram(word, check):
    s_word = sorted(word)
    s_check = sorted(check)

    if (s_word == s_check):
        return True
    else:
        return False

if __name__=='__main__':
    print(is_anagram("anagram", "nagaram"))
