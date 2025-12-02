def p1():
    dial = 50
    count = 0
    with open("input.txt") as f:
        content = f.read()
    for line in content.split("\n"):
        if line.strip() != "":
            direction = line[0]
            number = int(line[1:])
            if direction == "L":
                dial = dial - number
            elif direction == "R":
                dial = dial + number
            dial = dial % 100
            if dial == 0:
                count = count + 1
    print("count", count)


def p2():
    dial = 50
    count = 0
    with open("input.txt") as f:
        content = f.read()
    for line in content.split("\n"):
        if line.strip() != "":
            direction = line[0]
            magnitude = int(line[1:])
            for _ in range(magnitude):
                if direction == "L":
                    dial = (dial - 1) % 100
                if direction == "R":
                    dial = (dial + 1) % 100
                if dial == 0:
                    count += 1
    print("count", count)


p1()
p2()
