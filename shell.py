def sor(A,first, last, gap):
    for i in range(first+gap, last+1, gap):
        key = A[i]
        j = i-gap
        while j >= first and key < A[j]:
            A[j+gap] = A[j]
            j=j-gap
        A[j+gap] = key
        print("step",i, '=', A)

def shell(A):
    n= len(A)
    gap = n//2
    while gap > 0:
        if (gap % 2) == 0 : gap+1
        for i in range(gap):
            sor(A,i,n-1,gap)
        print("gap",gap, '=', A)
        gap = gap //2

shell([15,36,65,15,22,53,7])