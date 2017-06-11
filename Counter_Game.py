import math

def poweroftwo(num):
    return num and (not(num&(num-1)))

def highestpoweroftwo(num):
    return(pow(2,math.floor(math.log(num)/math.log(2))))


def counter(num):
    #Louise = 0
    #Richard = 1
    counter = num
    player = 1

    if counter == 1:
        print("Richard")
        return

    while(counter!=1):
        if poweroftwo(counter):
            counter-=counter//2
        else:
            counter-=highestpoweroftwo(counter)
        player = int(not player)

    if player:
        print("Richard")
    else:
        print("Louise")

if __name__ == '__main__':
    T = int(input().strip());
    for i in range(T):
        num = int(input().strip())
        counter(num)
