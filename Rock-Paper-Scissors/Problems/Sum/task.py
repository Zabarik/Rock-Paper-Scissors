# read sums.txt
f = open("sums.txt")
lines = [line.split() for line in f.readlines()]
lines = [[int(line[0]), int(line[1])] for line in lines]
sums = [sum(line) for line in lines]
print(*sums, sep="\n")
f.close()
