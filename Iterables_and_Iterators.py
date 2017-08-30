import itertools

n = int(input())
indices = input().split()
k = int(input())
den = 0
num = 0
combo = itertools.combinations(indices,k)

for i in combo:
    if 'a' not in i:
        num+=1
    den+=1
      
prob = 1 - (num/den)
print(prob)
