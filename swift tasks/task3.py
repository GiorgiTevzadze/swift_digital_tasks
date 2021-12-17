def output(r,c,n,grid):
    if n%2==0:
        print('\n'.join('O'*c for y in range(r)))
        return
    m=2*max(r,c)
    if n>m:
        n=m+(n-m)%4
    for i in range(n//2):
        grid=go(r,c,n,grid)
    print('\n'.join(''.join(g) for g in grid))

def go(r,c,n,grid):
    g=[list('O'*c) for y in range(r)]
    for y in range(r):
        for x,b in enumerate(grid[y]):
            if b=='.':
                continue
            g[y][x]='.'
            if y>0:
                g[y-1][x]='.'
            if y<r-1:
                g[y+1][x]='.'
            if x>0:
                g[y][x-1]='.'
            if x<c-1:
                g[y][x+1]='.'
    return g

r,c,n=input().split(' ')
r,c,n=int(r),int(c),int(n)
grid=[]
for y in range(r):
    grid.append(input())
output(r,c,n,grid)
    