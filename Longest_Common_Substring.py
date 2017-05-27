		a b c d x y z
	0   0 0 0 0 0 0 0
a	0	1 0 0 0 0 0 0
b	0	0 2	0 0 0 0 0
c	0	0 0 3 0 0 0 0
d	0 	0 0 0 4 0 0 0

Longest Common String  here = 4

def LCS(X,Y,m,n):
    L = [[0 for i in range(n+1)] for j in range(m+1)]
    result =0
    for i in range(m+1):
        for j in range(n+1):
            #Exlude first row and first column entirely
            if i == 0 or j == 0:
                L[i][j] =0
            elif X[i-1] == Y[j-1]:
                L[i][j]=L[i-1][j-1]+1

                #this step is needed to store result and hence avoid looping
                result = max(result,L[i][j])
            else:
                L[i][j]=0
    return result

if __name__=='__main__':
    X = input().strip()
    Y = input().strip()
    m = len(X)
    n = len(Y)
    result = LCS(X,Y,m,n)
    print(result)
