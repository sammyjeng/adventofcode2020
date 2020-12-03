#!/usr/bin/python3


'''
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
'''


def part2(tree):
    total = 1
    slopes = [(3,1),(1, 1),(5, 1),(7, 1),(1, 2)]
    for (col, row) in slopes:
        rows = cols = 0
        t_tree = 0 
        while rows < len(tree):
            cols += col
            rows += row
            if  rows< len(tree) and tree[rows][cols%len(tree[rows])] == '#':
                t_tree += 1
        total *= t_tree
    #assert total == 336
    return total


def traverse(tree):
    rows = cols = 0
    t_tree = 0
    while rows < len(tree):
        cols += 3
        rows += 1
        '''
         wrap around with mod (These aren't the only trees, though;
         due to something you read about once involving arboreal genetics and biome stability,
         the same pattern repeats to the right many times:
        '''
        if  rows< len(tree) and tree[rows][cols%len(tree[rows])] == '#':
            t_tree += 1
    return t_tree


if __name__ == '__main__':

    with open('input.txt','r') as f:
        f = f.readlines()
    tree = []
    for line in f:
        tree.append((line.strip('\n')))

    print(traverse(tree))
    print(part2(tree))
