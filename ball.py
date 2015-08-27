N,K = map(int,raw_input().split())
a = [1,2,3,4,5,6,7,8]
for i in xrange(N):
    A,B = map(int,raw_input().split())
    temp = a[A-1]
    a[A-1] = a[B-1]
    a[B-1] = temp
    
print a