def Permutation(n):
    ret = 1
    for item in range(1,n+1):
        ret = item * ret
    return ret

a = 15
print(Permutation(a))