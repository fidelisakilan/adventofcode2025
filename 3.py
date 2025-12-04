# content = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""


def p1():
    with open("input.txt") as f:
        content = f.read().strip()
    jolt = 0
    for bank in content.split("\n"):
        i = 0
        maxL = 0
        while i < len(bank) - 1:
            if bank[maxL] < bank[i]:
                maxL = i
            i += 1
        j = maxL + 1
        maxR = maxL + 1
        while j < len(bank):
            if bank[maxR] < bank[j]:
                maxR = j
            j += 1
        jolt += int(f"{bank[maxL]}{bank[maxR]}")
    print(jolt)


def p2():
    jolt = 0
    with open("input.txt") as f:
        content = f.read().strip()
    for bank in content.split("\n"):
        battery = ""
        i = 0
        while len(battery) != 12:
            maxV = 0
            maxI = 0
            while i < len(bank) + len(battery) - 12 + 1:
                if maxV < int(bank[i]):
                    maxV = int(bank[i])
                    maxI = i
                i += 1
            battery += str(maxV)
            i = maxI + 1
        jolt += int(battery)
    print(jolt)


p1()
p2()
