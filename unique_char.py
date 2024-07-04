def isUnique(str):
    str = str.lower()
    if len(str) > 128:
        return False
    char_set = [False] * 128
    for i in range(len(str)):
        val = ord(str[i])
        if char_set[val]:
            return False
        char_set[val] = True
    return True

str = "Aman"
print(isUnique(str))