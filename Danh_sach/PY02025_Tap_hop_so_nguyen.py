def Tap_hop(a,b):
    print(*sorted(a&b))
    print(*sorted(a-b))
    print(*sorted(b-a))

n, m = map(int, input().split())
a = set(input().split())
b = set(input().split())
Tap_hop(a,b)