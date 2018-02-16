'''
Algo : O(M*N) Worst case when hashes match but substrings are not equal
1.Compute hash of pattern (size M) - X
2.Compute hash of each substring of size M in input text- Y
3.If X == Y , check if substrings are equal -- >return index
4.If not , continue with next substring of text

Reference : https://github.com/mission-peace/interview
'''

#take larger value
prime = 3

def CreateHash(string,size):
    hashed = 0
    for i in range(size):
        hashed +=ord(string[i])*pow(prime,i)

    return hashed

def CheckEqual (text,pattern):
    if len(text)!=len(pattern):
        return False

    for i,j in zip(text,pattern):
        if i!=j:
            return False
    return True

def RecalculateHash(text,oldchar,newchar,oldhash,m):
    newhash = oldhash - ord(text[oldchar])
    newhash = newhash / prime
    newhash += pow(prime,m-1)*ord(text[newchar])
    return newhash

def PatternSearch(text,pattern,n,m):
    texthash = CreateHash(text,m)
    patternhash = CreateHash(pattern,m)
    found = False

    for i in range(1,n-m+2):

        if patternhash == texthash:
            if CheckEqual(text[i-1:i+m-1], pattern[0:]) is True:
                print("Pattern found at index ",i-1)
                found = True

        if i<n-m+1:
            texthash = RecalculateHash(text,i-1,i+m-1,texthash,m)

    if Found is False:
        print("Pattern not found!")


if __name__ == '__main__':
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    PatternSearch(text,pattern,len(text),len(pattern))
