N = int(raw_input())
arr = [0]*N
for i in xrange(N):
    A,D = map(int,raw_input())
    if D >= 0:
        arr[D-1] = A

