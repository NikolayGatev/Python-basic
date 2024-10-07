from math import dist, floor

def close_center_point(a:[]) -> ():
    b = dist(a[:2], a[2:4])
    c = dist(a[4:6], a[6:])

    return ((floor(a[0]), floor(a[1])), (floor(a[2]), floor(a[3]))) if(b >= c) else ((floor(a[4]), floor(a[5])), (floor(a[6]), floor(a[7])))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
c1 = float(input())
d1 = float(input())
c2 = float(input())
d2 = float(input())

print(close_center_point([x1, y1, x2, y2, c1, d1, c2, d2]))