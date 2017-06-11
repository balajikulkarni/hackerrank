'''
     a b c d a f
   0 0 0 0 0 0 0
a  0 1 1 1 1 1 1
c  0 1 1 2 2 2 2
b  0 1 2 2 2 2 2
c  0 1 2 3 3 3 3
f  0 1 2 3 3 3 4

Algo:
1.If i==0 or j==0 , D[i][j]=0
2..If str1[i] == str2[j]
    D[i][j] = D[i-1][j-1]+1
  else
    D[i][j] = max(D[i-1][j],D[i][j-1])
3.Return D[m][n]
'''

def LongestCommonSequence(X,Y,m,n):
    D = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m):
        D[i][0]=0
    for i in range(n):
        D[0][i]=0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                D[i][j] = D[i-1][j-1] +1
            else:
                D[i][j] = max(D[i-1][j],D[i][j-1])
    return(D[m][n])

if __name__=='__main__':
    X = input('Str1 ').strip()
    Y = input('Str2 ').strip()
    print(LongestCommonSequence(X,Y,len(X),len(Y)))
