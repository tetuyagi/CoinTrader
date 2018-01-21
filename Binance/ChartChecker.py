# coding: utf-8

from BinanceClient import BinanceClient
from Analyze import MA
from Graphic import *
from Candle import Candle
from Judgment import *
from Helper import *
from binance.helpers import *
from Mailer import Mailer

import time


class Event:
    def __init__(self, symbol, message):
        self.symbol = symbol
        self.message = message


def judge(client, symbol, maList, startTime, endTime):
    eventList = []

    ma7 = maList[0]
    ma25 = maList[1]
    ma99 = maList[2]

    shortMA = ma7.averageList
    shortMA.reverse()
    longMA = ma25.averageList
    longMA.reverse()

    if(isGoldenCross(shortMA, longMA, startTime, endTime)):
        print("gold cloth!")
        eventList.append(Event(symbol, "Golden Cross"))


    if(isDeadCross(shortMA, longMA, startTime, endTime)):
        print("dead cloth!")
        eventList.append(Event(symbol, "Dead Cross"))

    return eventList


def plot(candleList, maList, plotDataList):
    for i in range(len(maList)):
        plotData = PlotData.pointListToPlotData(maList[i].averageList)
        plotDataList.append(plotData)

    for i in range(len(plotDataList)):
        plotData = plotDataList[i]
        plotArray(plotData.dataX, plotData.dataY)

    plotChart(candleList)
    showPlot()


def checkSymbol(client, symbol):
    # chartを作る
    ohlcList = client.getOhlcList(symbol)

    candleList = Candle.convertToCandleList(ohlcList)

    # index=0が最新
    endTime = candleList[0].ohlc.openTime
    startTime = endTime - hourToMillisecond(2)

    # MA作る
    pointList = Candle.convertToClosePointList(candleList)

    ma7 = MA(7, pointList)
    ma25 = MA(25, pointList)
    ma99 = MA(99, pointList)

    #now = "now +0900"
    #dt1 = "2018/1/6 9:0:0 +0900"
    #dt2 = "2018/1/6 11:0:0 +0900"

    eventList = judge(client, symbol, [ma7, ma25, ma99], startTime, endTime)

    data1 = PlotData([startTime, startTime], [0, 0.00001500])
    data2 = PlotData([endTime, endTime], [0, 0.00001500])

    # plot(candleList, [ma7, ma25, ma99], [data1, data2])

    return eventList


mailer = Mailer()
subject = "仮想通貨　速報"

bc = BinanceClient()
interval = 2 * 3600  # 2時間

while(True):
    eventList = []
    symbolList = bc.getSymbolList()

    for i in range(len(symbolList)):
        symbol = symbolList[i]
        el = checkSymbol(bc, symbol)

        for j in range(len(el)):
            eventList.append(el[j])

    if(len(eventList) != 0):
        body = ""
        for i in range(len(eventList)):
            event = eventList[i]
            body += "{0} : {1}\n".format(event.symbol, event.message)

        mailer.send(subject, body)

    time.sleep(interval)
