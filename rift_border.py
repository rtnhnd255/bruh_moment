import math
from typing import List

from vertex import Vertex, calc_distance


def calc_border(matrix: List[List[float]]) -> List[int]:
    result: List[int] = []
    _len: int = len(matrix[0])
    while len(result) < _len - 1:
        idx = matrix[0].index(min(matrix[0]))
        result.append(idx)
        del matrix[0]
        for i in range(len(matrix)):
            del matrix[i][idx]
    result.append(matrix[0][0])
    return result


def calc_graph(vertexes: List[Vertex]) -> List[List[float]]:
    result: List[List[float]] = []

    for i in range(len(vertexes)):
        subres = []
        for j in range(len(vertexes)):
            if i == j:
                subres.append(0.0)
            else:
                subres.append(calc_distance(vertexes[i], vertexes[j]))
        result.append(subres)

    return result
