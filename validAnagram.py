def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    count = {}
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in str2:
        if char in count:
            count[char] -= 1
        else:
            return False
    return True


print(anagram(str1="anagram", str2="panagram"))
