# coding: utf-8

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import pandas as pd


class PlotData:
    def __init__(self, dataX = [], dataY = []):
        self.dataX = dataX
        self.dataY = dataY

    @staticmethod
    def pointListToPlotData(pointList):
        pData = PlotData()
        for i in range(len(pointList)):
            point = pointList[i]
            pData.dataX.append(point.x)
            pData.dataY.append(point.y)

        return pData


# xは右端（今日）を0とし、左に行けば過去にいく
class Point:
    def __init__(self, x=0, y=0, index=0):
        self.x = x
        self.y = y
        self.index = index

def plotArray(dataX, dataY):
    plt.plot(dataX, dataY)

def plotPointList(pointList):
    dataX = []
    dataY = []
    for i in range(len(pointList)):
        dataX.append(pointList.x)
        dataY.append(pointList.y)

    plt.plot(dataX, dataY)

# plot ma
def plotMA(ma):
    dataX = []
    dataY = []
    for i in range(len(ma.averageList)):
        averagePoint = ma.averageList[i]
        dataX.append(averagePoint.x)
        dataY.append(averagePoint.y)

    plt.plot(dataX, dataY)


def plotChart(candlePointList):
    data = []
    for i in range(len(candlePointList)):
        ohlc = candlePointList[i].ohlc
        data.append(ohlc.toArray())

    ax = plt.subplot()

    candlestick_ohlc(
        ax,
        data,
        width=1.0,
        colorup='skyblue',
        colordown='black'
    )


# plot all
# def showPlot(candlePointList, maList):
def showPlot():
    df = pd.DataFrame({
    '時刻':pd.to_datetime(['201'])
    })
    df = d
    plt.show()
