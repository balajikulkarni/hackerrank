#!/bin/python3

import sys
from collections import Counter


def isValid(s):
    count = []
    validate =0
    for _,cnt in Counter(s).items():
        count.append(cnt)

    count = sorted(count)

    for i in range(1,len(count)):
        if count[i]-count[i-1] >= 1:
            validate +=1

    if validate >=1:
        return('NO')
    else:
        return('YES')

s = input().strip()
result = isValid(s)
print(result)
