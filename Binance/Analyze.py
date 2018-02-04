# coding: utf-8

from Graphic import Point

import numpy as np


# 単純平均移動線
class MA:
    def __init__(self, rangeNum, pointList):
        self.range = rangeNum
        self.averageList = []

        self.__calculateAverageList(rangeNum, pointList)

    # 平均値のpointListをつくる
    def __calculateAverageList(self, rangeNum, pointList):
        listLength = len(pointList)
        averageListLength = listLength - rangeNum + 1

        # rangeがpointListの長さ以上になっていないかチェック
        if(averageListLength < 0):
            print("doesnt have enough point to make ma")
            return

        for i in range(averageListLength):
            # 基準点（右端）
            basePoint = pointList[i]
            index = basePoint.index
            x = basePoint.x

            # 平均を取る範囲のy座標の配列を作る
            dataArray = []
            for j in range(rangeNum):
                point = pointList[i+j]
                # print("point = " + str(point))
                y = point.y
                # print("y = " + str(y))
                dataArray.append(y)

            # 平均点をリストに追加
            point = self.__calculateAverage(x, index, dataArray)
            self.averageList.append(point)

    # 平均値を出す関数
    def __calculateAverage(self, x, index, dataArray):
        average = np.average(dataArray)
        return Point(x, average, index)
