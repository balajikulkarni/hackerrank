'''
		a b c d x y z
	0   0 0 0 0 0 0 0
a	0	1 0 0 0 0 0 0
b	0	0 2	0 0 0 0 0
c	0	0 0 3 0 0 0 0
d	0 	0 0 0 4 0 0 0

Longest Common Sub-String  here = 4
Constraint: Should be contiguous

Algo:
1.If i==0 or j==0 , D[i][j]=0
2..If str1[i] == str2[j]
    D[i][j] = D[i-1][j-1]+1
3.Return D[m][n]
'''

def LCS(X,Y,m,n):
    D = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m):
        D[i][0]=0
    for i in range(n):
        D[0][i]=0
    result = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                D[i][j] = D[i-1][j-1] +1
                result = max(result,D[i][j])
            else:
                D[i][j] = 0
    return(D[m][n])


if __name__=='__main__':
    X = input('Str1> ').strip()
    Y = input('Str2> ').strip()
    m = len(X)
    n = len(Y)
    result = LCS(X,Y,m,n)
    print(result)
