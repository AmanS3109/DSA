import math
# sum of squared number
def judgeSquareSum(c):
        a = 0
        b = int(math.sqrt(c))  # Ensure integer square root for efficiency

        while a <= b:
            square_sum = a * a + b * b
            if square_sum == c:
                return True
            elif square_sum < c:
                a += 1
            else:
                b -= 1

        return False

c = 5
print(judgeSquareSum(c))