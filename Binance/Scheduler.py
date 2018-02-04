# coding: utf-8

import datetime


class Scheduler:
    def __init__(self):
        self.timeTable = [
            1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23
        ]

        self.checkPoint = 0
        self.checkPointIndex = 0

    def __setCheckPoint(self):
        for i in range(len(self.timeTable)):
            start = self.timeTable[i]

            if(i == len(self.timeTable)-1):
                end = 25
            else:
                end = self.timeTable[i + 1]

            if(t in range(start, end)):
                self.checkPointIndex = self.__nextIndex(i)
                self.checkPoint = self.timeTable[self.checkPointIndex]

    def __nextIndex(self, index):
        if(index >= len(self.timeTable) - 1):
            return 0
        else:
            return index + 1

    def __setNextCheckPoint(self):
        self.checkPointIndex = self.__nextIndex(self.checkPointIndex)
        self.checkPoint = self.timeTable[self.checkPointIndex]

    def isOverCheckPoint(self):
        now = datetime.datetime.now()
        hour = now.hour
        if(hour > self.checkPoint):
            self.__setNextCheckPoint()
            return True

        else:
            return False




prevHour = 0
nowHour = 0

checkPoint = 0
checkPointIndex = 0
