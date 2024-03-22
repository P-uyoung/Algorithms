def find_fraction_revised(n):
    level = 1
    while n > level:
        n -= level
        level += 1

    if level % 2 == 0:
        numerator = n
        denominator = level - n + 1
    else:
        numerator = level - n + 1
        denominator = n

    return f"{numerator}/{denominator}"

# Retry with the corrected logic
print(find_fraction_revised(int(input())))