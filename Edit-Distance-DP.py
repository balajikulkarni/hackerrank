'''
Example:

    a b c d e f
  0 1 2 3 4 5 6
a 1 0 1 2 3 4 5
z 2 1 1 2 3 4 5
c 3 2 2 1 2 3 4
e 4 3 3 2 2 3 4
d 5 4 4 3 3 3 4

Time and Space : O(m*n)
'''

def EditDistance(str1,str2):
    m = len(str1)
    n = len(str2)

    D = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m):
        D[i][0] = i

    for i in range(n):
        D[0][i] = i

    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j]=min(D[i-1][j-1],D[i][j-1],D[i-1][j])+1

    return(D[m][n])

if __name__ == '__main__':
    str1 = "abcdef"
    str2 = "azced"
    result = EditDistance(str1,str2)
    print(result)
