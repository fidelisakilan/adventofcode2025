def p1():
    with open("input.txt") as f:
        content = f.read().strip()
    range_list = content.split("\n\n")[0].split("\n")
    id_list = content.split("\n\n")[1].split("\n")
    count = 0
    for id in id_list:
        fresh = False
        for r in range_list:
            start = r.split("-")[0]
            end = r.split("-")[1]
            if int(start) <= int(id) <= int(end):
                fresh = True
                # print(id, start, end)
        if fresh:
            count += 1
    print(count)


def p2():
    with open("input.txt") as f:
        content = f.read().strip()
    range_list = sorted(
        [
            (int(text.split("-")[0]), int(text.split("-")[1]))
            for text in content.split("\n\n")[0].split("\n")
        ]
    )
    total = 0
    current_low, current_high = range_list.pop(0)
    while len(range_list) > 0:
        next_low, next_high = range_list.pop(0)
        if next_low <= current_high:
            current_high = max(current_high, next_high)
        else:
            total += current_high - current_low + 1
            current_low, current_high = next_low, next_high
    total += current_high - current_low + 1
    print(total)


p1()
p2()
