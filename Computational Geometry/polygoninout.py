#1. Draw horizontal line to right of each point and extend to infinity
#2. Count number of times the line intersects with polygon edges.
#3. If number of intersections is odd, then point is inside polygon or on edge. If none true, then point outside.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def onLine(l1, p):
    if (
        p.x <= max(l1.p1.x, l1.p2.x) and
        p.x <= min(l1.p1.x, l1.p2.x) and
        (p.y <= max(l1.p1.y, l1.p2.y) and
        p.y <= min(l1.p1.y, l1.p2.y))
    ):
        return True
    return False

def direction(a, b, c):
    val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y-b.y)
    if val == 0:
        return 0
    elif val < 0:
        return 2
    return 1

def intersect(l1, l2):
    d1 = direction(l1.p1, l1.p2, l2.p1)
    d2 = direction(l1.p1, l1.p2, l2.p2)
    d3 = direction(l2.p1, l2.p2, l1.p1)
    d4 = direction(l2.p1, l2.p2, l1.p2)

    if d1 != d2 and d3 != d4:
        return True
    if d1 == 0 and onLine(l1, l2.p1):
        return True
    if d2 == 0 and onLine(l1, l2.p2):
        return True
    if d3 == 0 and onLine(l2, l1.p1):
        return True
    if d4 == 0 and onLine(l2, l1.p2):
        return True
    return False

def isInside(polygon, p):
    n = len(polygon)
    if n < 3:
        return False

    extreme = Point(100000, p.y)
    count = 0
    i = 0
    while i < n:
        next = (i+1) % n
        if intersect(Line(polygon[i], polygon[next]), Line(p, extreme)):
            if direction(polygon[i], p, polygon[next]) == 0:
                return onLine(Line(polygon[i], polygon[next]), p)
            count += 1
        i = next
    return count % 2 == 1

