import math
from typing import List


class Vertex:
    x: float
    y: float

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def calc_distance(a: Vertex, b: Vertex) -> float:
    return math.pow(math.pow(b.x - a.x, 2.0) + math.pow(b.y - a.y, 2.0), 0.5)


def xs(vert: List[Vertex]) -> List[float]:
    result: List[float] = []
    for v in vert:
        result.append(v.x)
    return result


def ys(vert: List[Vertex]) -> List[float]:
    result: List[float] = []
    for v in vert:
        result.append(v.y)
    return result
