from aoc import *  # get_input, d4, d8, d4n

input = get_input(2022, 2)

hands = [(ord(i[0]) - ord('A'), ord(i[2]) - ord('X')) for i in input.splitlines()]

p1 = sum([h[1] + 1 + 3 * (h[0] == h[1]) + 6 * ((h[0] + 1) % 3 == h[1]) for h in hands])
print("part 1:",p1)

p2 = sum([(h[0] + (h[1] - 1)) % 3 + 1 + 3 * h[1] for h in hands])
print("part 2:",p2)