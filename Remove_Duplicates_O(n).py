'''
Algorithm:
Time Complexity O(n)
1.Create a mutable string since strings are immutable.
2.Maintain two indexes (ip_ind and res_ind)
3.Create a hashmap of 256 characters
4.For all chars in mutableString , if its not seen previously (hashmap[ord(char)] is 0)
  Do the following;
    hashmap[ord(char)] = 1
    increment res_ind (res_ind+=1)
5.Else increment ip_ind (ip_ind+=1)
6.Join all characters till res_ind into a string and return it.

'''

NO_OF_CHARS = 256

def toMutable(string):
    return([c for c in string])

def removeDups(str):
    ip_ind = 0
    res_ind = 0
    mutableString = toMutable(string)
    binmap = [0]*NO_OF_CHARS
    while ip_ind != len(mutableString):
        temp = mutableString[ip_ind]
        if binmap[ord(temp)] == 0:
            binmap[ord(temp)] = 1
            mutableString[res_ind] = mutableString[ip_ind]
            res_ind+=1
        ip_ind+=1

    return (''.join(mutableString[0:res_ind]))

if __name__ == '__main__':
    string = input()
    print(removeDups(string))
