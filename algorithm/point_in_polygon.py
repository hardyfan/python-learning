#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 2019/9/16
    function: 判断给定点是否在多边形范围内
    versions: V 1.0
    @author: Hardy
    @copyright: Apache License, Version 2.0
"""


def in_polygon(pt, py):
    c = False
    i = -1
    l = len(py)
    j = l - 1
    while i < l - 1:
        i += 1
        # pt是否在线段的维度区间
        if ((py[i]["latitude"] <= pt["latitude"] and pt["latitude"] < py[j]["latitude"]) or (
                py[j]["latitude"] <= pt["latitude"] and pt["latitude"] < py[i]["latitude"])):
            # pt是否在区域内
            if (pt["longitude"] <= (py[j]["longitude"] - py[i]["longitude"]) *
                    (pt["latitude"] - py[i]["latitude"]) /
                    (py[j]["latitude"] - py[i]["latitude"]) +
                    py[i]["longitude"]):
                c = not c
        j = i
    return c


if __name__ == "__main__":
    # pt = {"latitude": 26.52, "longitude": 114.33}
    # py = [{"latitude": 25.52193172801192, "longitude": 113.2339186535454},
    #         {"latitude": 28.83866231651736, "longitude": 113.4675555951041},
    #         {"latitude": 30.22368646711938, "longitude": 116.5513437722832},
    #         {"latitude": 29.56371453005522, "longitude": 118.405291510863},
    #         {"latitude": 27.85209167310988, "longitude": 118.9107128394714},
    #         {"latitude": 25.45949511201445, "longitude": 117.6920579498773},
    #         {"latitude": 23.83764055483396, "longitude": 115.4529876768739},
    #         {"latitude": 24.68844541461111, "longitude": 113.7756476507107},
    #         {"latitude": 28.83866231651736, "longitude": 113.4675555951041}]
    pt = {"latitude": 0.5, "longitude": 0.5}
    py = [
        {"latitude": 0, "longitude": 0},
        {"latitude": 1, "longitude": 1},
        {"latitude": 1, "longitude": 0},
    ]
    print(in_polygon(pt, py))
