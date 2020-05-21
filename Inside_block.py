from typing import Tuple
def is_inside(polygon: Tuple[Tuple[int, int]], point: Tuple[int, int]) -> bool:
    v = lambda A, B: round(((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** (1 / 2), 1)
    polysides = []
    pointsides = []
    for e, i in enumerate(polygon):
        print(e)
        if e < len(polygon) - 1:
            polysides.append(v(polygon[e], polygon[e+1]))
            pointsides.append(v(polygon[e], point))
        else:
            polysides.append(v(polygon[e], polygon[0]))
            pointsides.append(v(polygon[e], point))
    print(polysides, pointsides)
    return True or False

# calculate sum of areas △APD,△DPC,△CPB,△PBA.
is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (2, 2))
is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3))