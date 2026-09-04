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

#print the name(s) of any student(s) having the second lowest grade.
def students(records):
    grades = sorted(set(record[1] for record in records))
    second_lowest_grade = grades[1]

    names = sorted(
        record[0]
        for record in records
        if record[1] == second_lowest_grade
    )

    return names

#List
def process_commands(commands):
    my_list = []

    for command in commands:
        command = command.split()

        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))

        elif command[0] == "print":
            print(my_list)

        elif command[0] == "remove":
            my_list.remove(int(command[1]))

        elif command[0] == "append":
            my_list.append(int(command[1]))

        elif command[0] == "sort":
            my_list.sort()

        elif command[0] == "pop":
            my_list.pop()

        elif command[0] == "reverse":
            my_list.reverse()
