# coding: utf-8
# from BinanceClient import Ohlc
from Graphic import Point


class Candle:
    def __init__(self, index, ohlc):
        self.index = index
        self.ohlc = ohlc

    def __getClosePoint(self):
        return Point(self.ohlc.openTime, self.ohlc.close, self.index)

    # ろうそくの座表データリスト作成
    @staticmethod
    def convertToCandleList(ohlcList):
        candleList = []
        for i in range(len(ohlcList)):
            ohlc = ohlcList[i]
            candleList.append(Candle(i, ohlc))

        return candleList

    # MA用の点
    @staticmethod
    def convertToClosePointList(candleList):
        pointList = []
        for i in range(len(candleList)):
            candle = candleList[i]
            pointList.append(candle.__getClosePoint())

        return pointList
