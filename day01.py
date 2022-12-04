from aoc import * # get_input, d4, d8, d4n


inp = get_input(2022, 1)
cpf = [sum([int(c) for c in e.split("\n")]) for e in inp.strip().split("\n\n")]

print( "part 1:",max(cpf) )
print( "part 2:",sum(sorted(cpf, reverse=True)[:3]) )
