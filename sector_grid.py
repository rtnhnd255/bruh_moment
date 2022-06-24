from cgitb import reset
import re
from turtle import right
from typing import List, Tuple
from unittest import result
from vertex import Vertex
import vertex


class Grid:
    left_top: Vertex
    right_bot: Vertex
    grid_intersection: List[List[Vertex]]  # list of four lists of vertexes
    sector_size: float

    def __init__(self, sector_size: float, left_top: Vertex, rigth_bot: Vertex, grid_intersection: List[List[Vertex]]) -> None:
        self.sector_size = sector_size
        self.left_top = left_top
        self.right_bot = rigth_bot
        self.grid_intersection = grid_intersection


def calc_grid(vertexes: List[Vertex], sector_size: float) -> Grid:
    left_top, right_bottom = calc_corner_vertexes(
        vertexes=vertexes, sector_size=sector_size)
    return Grid(sector_size=sector_size, left_top=left_top, rigth_bot=right_bottom, grid_intersection=calc_grid_intersections(left_top, right_bottom, sector_size))


# returns left top and right bottom
def calc_corner_vertexes(vertexes: List[Vertex], sector_size: float) -> Tuple[Vertex, Vertex]:
    x_mas: List[float] = vertex.xs(vertexes)
    y_mas: List[float] = vertex.ys(vertexes)

    x_max: float = max(x_mas)
    x_min: float = min(x_mas)
    y_max: float = max(y_mas)
    y_min: float = min(y_mas)

    x_distance: float = x_max - x_min
    y_distance: float = y_max - y_min

    if float(int(x_distance / sector_size)) != x_distance / sector_size:
        delta_x: float = (int(x_distance / sector_size) +
                          1) * sector_size - x_distance
    else:
        delta_x = 0

    if float(int(y_distance / sector_size)) != y_distance / sector_size:
        delta_y: float = (int(y_distance / sector_size) +
                          1) * sector_size - y_distance
    else:
        delta_y = 0

    return Vertex(x_min - delta_x/2, y_max + delta_y / 2), Vertex(x_max + delta_x/2, y_min - delta_y / 2)


def calc_grid_intersections(left_top: Vertex, right_bot: Vertex, sec_size: float):
    result: List[List[Vertex]] = [[], [], [], []]
    x_actual: float = left_top.x
    y_actual: float = left_top.y

    # x loop
    while x_actual != right_bot.x:
        result[0].append(Vertex(x_actual, left_top.y))  # top Ox edge
        result[1].append(Vertex(x_actual, right_bot.y))  # bot Ox edge
        x_actual += sec_size

    while y_actual != right_bot.y:
        result[2].append(Vertex(left_top.x, y_actual))  # left Oy edge
        result[3].append(Vertex(right_bot.x, y_actual))  # right Oy edge
        y_actual -= sec_size

    return result
