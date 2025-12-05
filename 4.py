def p1(content):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]

    content = [list(line) for line in content.split("\n")]
    width = len(content[0])
    height = len(content)
    count = 0

    for i in range(0, len(content)):
        for j in range(0, len(content[0])):
            adj_count = 0
            loc = content[i][j]
            if loc != "@":
                continue
            for dir in directions:
                if i + dir[1] < 0 or i + dir[1] > height - 1:
                    continue
                if j + dir[0] < 0 or j + dir[0] > width - 1:
                    continue
                if content[i + dir[1]][j + dir[0]] == "@":
                    adj_count += 1
            if adj_count < 4:
                count += 1
    print(count)


def p2(content):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]

    content = [list(line) for line in content.split("\n")]
    width = len(content[0])
    height = len(content)

    def modify_matrix(content):
        count = 0
        for i in range(0, len(content)):
            for j in range(0, len(content[0])):
                adj_count = 0
                loc = content[i][j]
                if loc != "@":
                    continue
                for dir in directions:
                    if i + dir[1] < 0 or i + dir[1] > height - 1:
                        continue
                    if j + dir[0] < 0 or j + dir[0] > width - 1:
                        continue
                    if content[i + dir[1]][j + dir[0]] == "@":
                        adj_count += 1
                if adj_count < 4:
                    count += 1
                    content[i][j] = "."
        if count > 0:
            return count + modify_matrix(content)
        return count

    print(modify_matrix(content))


content = """..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@."""

with open("input.txt") as f:
    content = f.read().strip()
p1(content)

content = """..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@."""

with open("input.txt") as f:
    content = f.read().strip()
p2(content)
