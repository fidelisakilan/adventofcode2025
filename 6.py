def p1():
    with open("input.txt") as f:
        content = f.read().strip()

    rows = [line.split() for line in content.split("\n")]
    operations = rows.pop()
    row_length = len(rows)
    col_length = len(operations)
    total = 0
    for i in range(col_length):
        op = operations[i]
        if op == "*":
            result = 1
        else:
            result = 0
        for j in range(row_length):
            if op == "*":
                result = result * int(rows[j][i])
            elif op == "+":
                result = result + int(rows[j][i])
        total += int(result)
    print(total)


def p2():
    content = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    with open("input.txt") as f:
        content = f.read()
    rows = [line for line in content.split("\n")]
    rows.pop()
    i = 0
    total = 0
    current_op = None
    row_length = len(rows)
    col_length = len(rows[-1])
    result = 0
    while True:
        op = rows[-1][i]
        if op == "*":
            total = result + total
            result = 1
            current_op = op
        elif op == "+":
            total = result + total
            result = 0
            current_op = op
        number = ""
        for r in range(row_length - 1):
            number = f"{number}{rows[r][i]}"
        # print(number)
        if number.strip() != "":
            if current_op == "*":
                result = result * int(number.strip())
            elif current_op == "+":
                result = result + int(number.strip())
        if i == col_length - 1:
            total = total + result
            break
        i += 1
    print(f"\n{total}")


# p1()
p2()
