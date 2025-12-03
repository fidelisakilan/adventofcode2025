def p1():
    with open("input.txt") as f:
        content = f.read()
    # content = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    sum = 0
    for ranges in content.split(","):
        firstId = int(ranges.split("-")[0])
        lastId = int(ranges.split("-")[1])
        # print(firstId, lastId)
        for idx in range(firstId, lastId + 1):
            num_str = str(idx)
            num_length = len(num_str)
            if num_length % 2 != 0:
                continue
            elif num_str[: (num_length // 2)] == num_str[(num_length // 2) :]:
                print(num_str)
                sum += idx
    print(sum)


def p2():
    with open("input.txt") as f:
        content = f.read()
    # content = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    sum = 0
    for ranges in content.split(","):
        firstId = int(ranges.split("-")[0])
        lastId = int(ranges.split("-")[1])
        for idx in range(firstId, lastId + 1):
            num_str = str(idx)
            num_length = len(num_str)
            for count in range(1, num_length + 1):
                invalid = True
                x = idx
                rem = None
                while True:
                    if rem is None:
                        rem = str(x)[-count:]
                        x = x // (10**count)
                        continue
                    n_rem = str(x)[-count:]
                    x = x // (10**count)
                    if n_rem != rem:
                        invalid = False
                        break
                    rem = n_rem
                    if x == 0:
                        break
                if invalid:
                    print(idx, count)
                    sum = sum + idx
                    break
    print(sum)


p1()
p2()
