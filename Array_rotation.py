for i in range(int(input())):  # number of test cases
    n,rotate=map(int,input().split()) #n (size of array) # rotate=no of rotations
    a=list(map(int,input().split()))
    b=a[:]
    for j in range(n):
        a[j]=b[(j+rotate)%(n)]
    print(a)
