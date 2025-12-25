from collections import defaultdict


def p1():
    content = """.......S.......
    ...............
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ..............."""

    with open("input.txt") as f:
        content = f.read()

    manifold = [list(line) for line in content.split("\n")]

    s_index = manifold[0].index("S")
    depth = 0
    beam_indexes = [s_index]
    split_counter = 0
    while depth < len(manifold) - 1:
        new_depth = depth + 1
        new_beam_indexes = set()
        for bi in beam_indexes:
            value = manifold[new_depth][bi]
            if value == ".":
                new_beam_indexes.add(bi)
            elif value == "^":
                new_beam_indexes.add(bi - 1)
                new_beam_indexes.add(bi + 1)
                split_counter += 1
        print(new_depth, new_beam_indexes)
        beam_indexes = new_beam_indexes
        depth = new_depth
    print(split_counter)


def p2():
    content = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    history = {}
    with open("input.txt") as f:
        content = f.read()
    manifold = [list(line) for line in content.split("\n")]

    def traverse(depth, beam_index):
        nonlocal manifold, history

        if depth == len(manifold) - 1:
            return 1
        
        next_cell = manifold[depth+1][beam_index]
        result = 0
        val = history.get((depth + 1, beam_index), None)
        if val is not None:
            result = val
        elif next_cell == ".":
            result = traverse(depth + 1, beam_index)
        elif next_cell == "^":
            result = traverse(depth + 1, beam_index - 1) + traverse(depth + 1, beam_index + 1)
        history[(depth + 1, beam_index)] = result
        return result 

    print(traverse(0, manifold[0].index("S")))


# p1()
p2()

