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

#Find the runner-up score
def runner_up(scores):
    score = list(scores)
    leader = score[0]
    runner_up = None
    for n in score[1:]:
        if n > leader:
            runner_up = leader
            leader = n
        elif n != leader and (runner_up is None or n > runner_up):
            runner_up = n
    return runner_up