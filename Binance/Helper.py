# coding: utf-8
import datetime
import pytz
from binance.helpers import date_to_milliseconds

def dayToMillisecond(days):
    return days * 24 * 3600 * 1000

def hourToMillisecond(hours):
    return hours * 3600 * 1000

# ポイント抽出 point[i].x < point[i+1].xと仮定している
def extractPoints(points, startTime, endTime):
    """
    print("len(points) : {}".format(len(points)))
    print("startTime : {}".format(startTime))
    print("endTime : {}".format(endTime))
    print("points[0].x : {}".format(points[0].x))
    print("points[len(points)-1].x : {}".format(points[len(points)-1].x))
    """
    startIndex = __getStartIndex(points, startTime)
    endIndex = __getEndIndex(points, endTime, startIndex)
    """
    print("startIndex : {}".format(startIndex))
    print("endIndex : {}".format(endIndex))
    """

    pointList = []
    for i in range(startIndex, endIndex+1):
        pointList.append(points[i])

    # print("len(pointList):{}".format(len(pointList)))
    return pointList


def __getStartIndex(points, startTime):
    for i in range(len(points)):
        point = points[i]

        if(point.x >= startTime):
            # print("i:{0}, t:{1}".format(i, point.x))
            return i

    return -1


def __getEndIndex(points, endTime, startIndex=0):

    for i in range(startIndex, len(points)):
        point = points[i]

        if(point.x == endTime):
            return i
        elif(point.x > endTime):
            return i - 1

    return -1


def datetimeToMillisecond(dateTime):
    dateTime.strftime()
    ms = date_to_milliseconds("January 01, 2018")

    return ms
