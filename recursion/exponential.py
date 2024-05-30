# most efficient recursion

def raise_to_power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / raise_to_power(base, -exp)
    else:
        half = raise_to_power(base, exp // 2)
        if exp % 2 == 0:
            return half * half
        else:
            return base * half * half

print(raise_to_power(5, 6))