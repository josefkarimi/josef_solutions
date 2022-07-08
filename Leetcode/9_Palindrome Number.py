def torf(x):
    x = str(x)
    for i in range(len(x)//2):
        if x[i] == x[len(x)-i-1]:
            print(i)
            pass
        else:
            print(i)
            return False
    else:
        return True

print(torf(1001))