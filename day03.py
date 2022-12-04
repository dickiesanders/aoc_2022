from aoc import *  # get_input, d4, d8, d4n
import pandas as pd


inp = get_input(2022, 3)
value = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,53)))

p1 = sum((pd.Series( ( ''.join( set( row[slice(0,len(row)//2)] ).intersection( set( row[slice(len(row)//2,len(row) ) ]) ) )   ) for row in inp.strip().split("\n"))).map(value))


p = list(zip(*[iter( inp.strip().split("\n") )]*3))
l = []
for b in p:
    a = list(set.intersection(*map(set, [b[0], b[1], b[2]])))
    for x in a[0]:
        l.append(x)  
p2 = sum( pd.Series(l).map(value) )

# if __name__ == '__main__':
#     sys.exit(cli())

print("part 1:", p1)
print("part 2:", p2)