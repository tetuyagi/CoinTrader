# coding: utf-8
# from Graphic import Point

from Helper import extractPoints


# 交差関数を返す
def countCross(pointsA, pointsB):
    if len(pointsA) != len(pointsB):
        print("error. len(pointsA) != len(pointsB)")
        return 0

    crossCount = 0
    prev = 0
    now = 0
    for i in range(len(pointsA)):
        now = pointsA[i] - pointsB[i]
        if(now * prev < 0):
            crossCount += 1

        prev = now

    return crossCount


def isCrossToUp(pointsA, pointsB, startTime, endTime):

    pointsA = extractPoints(pointsA, startTime, endTime)
    pointsB = extractPoints(pointsB, startTime, endTime)



    # pointAがpointBの下から始まっていないものは除く
    if(pointsA[0].y >= pointsB[0].y):
        return False

    # pointAがpointBの上で終わっていないものは除く
    if(pointsA[len(pointsA)-1].y <= pointsB[len(pointsB)-1].y):
        return False

    return True


def isCrossToDown(pointsA, pointsB, startTime, endTime):
    pointsA = extractPoints(pointsA, startTime, endTime)
    pointsB = extractPoints(pointsB, startTime, endTime)

    # pointAがpointBの上から始まっていないものは除く
    if(pointsA[0].y <= pointsB[0].y):
        return False

    # pointAがpointBの下で終わっていないものは除く
    if(pointsA[len(pointsA)-1].y >= pointsB[len(pointsB)-1].y):
        return False

    return True


# ゴールデンクロス　＊注意　途中
def isGoldenCross(shortMA, longMA, prevTime, currentTime):
    return isCrossToUp(shortMA, longMA, prevTime, currentTime)


# デッドクロス　＊注意　途中
def isDeadCross(shortMA, longMA, prevTime, currentTime):
    return isCrossToDown(shortMA, longMA, prevTime, currentTime)
