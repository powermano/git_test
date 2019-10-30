import os 

file = r'/home/users/tao.cai/test1.txt'
with open(file, 'r') as f:
    all = [x.strip() for x in f.readlines()]

print(len(all))
