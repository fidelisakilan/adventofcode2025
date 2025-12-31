from collections import defaultdict
content = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

with open("input.txt") as f:
    content = f.read()




def getDistance(junction_boxes):
    distances = []
    for i in range(len(junction_boxes)-1):
        for j in range(i+1, len(junction_boxes)):
            x1,y1,z1 = junction_boxes[i]
            x2,y2,z2 = junction_boxes[j]
            distance = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
            distances.append((distance,i, j))
    return distances

def union(parents, i, j):
    pi = parents[i]
    pj = parents[j]
    parents[pj] = pi

def find(parents, i):

    if parents[i] == i:
        return i
    
    parents[i] = find(parents, parents[i])
    return parents[i]


def p1():
    junction_boxes = [line.split(",") for line in content.split("\n")]
    junction_boxes = [(int(x),int(y),int(z)) for x,y,z in junction_boxes]
    circuits = {i:i for i in range(len(junction_boxes))}
    distances = getDistance(junction_boxes)
    distances.sort()
    for pair in range(1000):
        _, i, j = distances[pair]
        # print(junction_boxes[i], junction_boxes[j])
        if find(circuits, i) == find(circuits, j):
            continue
        union(circuits, i, j)
    sizes = defaultdict(int)

    for node in circuits.values():
        root = find(circuits, node)
        sizes[root] += 1
    
    ans = 1
    # print(sizes)
    for s in sorted(sizes.values())[-3:]:
        ans *= s
    print(ans)

def p2():
    junction_boxes = [line.split(",") for line in content.split("\n")]
    junction_boxes = [(int(x),int(y),int(z)) for x,y,z in junction_boxes]
    circuits = {i:i for i in range(len(junction_boxes))}
    distances = getDistance(junction_boxes)
    distances.sort()
    for _, i, j in distances:
        if find(circuits, i) == find(circuits, j):
            continue
        union(circuits, i, j)

        if all(find(circuits, 0) == find(circuits, i) for i in range(len(junction_boxes))):
            break
    x1,_,_ = junction_boxes[i]
    x2,_,_ = junction_boxes[j]

    print(x1*x2)
    

p1()
p2()