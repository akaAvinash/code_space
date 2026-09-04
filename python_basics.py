# Lis comprehension
def dimension_check(x,y,z,n):
    i = x
    j = y
    k = z
    result = [
        [x,y,z]
        for x in range(i + 1)
        for y in range(j + 1)
        for z in range(k + 1)
        if x + y + z != n
    ]

    print(result)