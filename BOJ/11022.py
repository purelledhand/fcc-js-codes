import sys;

cnt = range(int(sys.stdin.readline()));
for i in cnt:
    a, b = map(int,sys.stdin.readline().split());
    print('Case #{}: {} + {} = {}'.format(i+1, a, b, a+b));