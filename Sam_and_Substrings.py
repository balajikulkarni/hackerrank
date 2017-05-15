def sam_substr(num):
    sum =[]
    num = list(map(int,num))
    result = num[0]
    sum.append(num[0])
    
    for i in range(1,len(num)):
        temp = (i+1)*num[i]+10*sum[i-1]
        temp = temp%(pow(10,9)+7)
        sum.append(temp)
        result = result + temp
    result = (result%(pow(10,9)+7))
    return result

if __name__ == '__main__':
    num = input()
    print(sam_substr(num))
