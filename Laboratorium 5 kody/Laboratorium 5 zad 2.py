n = 5
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i>0 and j==0:
            a[i][j]=0
        elif i==0 and j>0:
            a[i][j]=1
        else:
            a[i][j]=(a[i-1][j]+a[i][j-1])/2
for row in a:
    print(' '.join([str(elem) for elem in row]))