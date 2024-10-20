#brute force
def countUnique(s):
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
            if count == 1:
                return i
    return -1

s = "apple"
print(countUnique(s))