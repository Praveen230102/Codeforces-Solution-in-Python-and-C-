import math
n, m, z = map(int, input().split())
u = m*n//math.gcd(m, n)
print(z//u)
