from typing import List, Tuple
Coords = List[Tuple[int, int]]

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    v = lambda A, B: round(((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** (1 / 2), 1)
    r = lambda x: round(x, 2)
    A, B, C, a, b, c = coords_1[0], coords_1[1], coords_1[2], coords_2[0], coords_2[1], coords_2[2]
    AB, AC, BC, ab, ac, bc = v(A, B), v(A, C), v(B, C), v(a, b), v(a, c), v(b, c)
    print(AB, AC, BC, ab, ac, bc)
    print(r(AB/ac), r(AC/ab), r(BC/bc))
    return r(AB/ab) == r(AC/ac) == r(BC/bc) or r(AB/bc) == r(AC/ac) == r(BC/ab) or r(AB/ac) == r(AC/ab) == r(BC/bc) or r(AB/ab) == r(AC/bc) == r(BC/ac)

print(similar_triangles([[1,0],[-3,-3],[2,-1]],[[-2,-3],[-5,0],[10,6]]))

#vector1 = lambda x1, y1, x2, y2: ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)