
def task(x):
    i = 2
    while x >= i:
        x -= x // i
        i += 1
    return x


line = list(map(int, input().split()))
print(task(line[1]) - task(line[0] - 1))
