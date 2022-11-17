T = int(input())

for i in range(T):
    date = input()
    Y = date[0:4]
    M = date[4:6]
    D = date[6:8]
    arr31 = [1,3,5,7,8,10,12]
    arr30 = [4,6,9,11]

    if int(M) in arr31:
        if int(D)>0 and int(D)<32:
            print("#{0} {1}/{2}/{3}".format(i+1, Y, M, D))
        else:
            print("#{} -1".format(i+1))
    elif int(M) in arr30:
        if int(D)>0 and int(D)<31:
            print("#{0} {1}/{2}/{3}".format(i+1, Y, M, D))
        else:
            print("#{} -1".format(i+1))
    elif int(M) == 2:
        if int(D)>0 and int(D)<29:
            print("#{0} {1}/{2}/{3}".format(i+1, Y, M, D))
        else:
            print("#{} -1".format(i + 1))
    else:
        print("#{} -1".format(i + 1))
