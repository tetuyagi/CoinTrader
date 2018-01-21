# coding: utf-8
from binance.client import Client
from settings import Settings
from Helper import dayToMillisecond

import datetime
import re


class Ohlc:
    def __init__(self, json):
        self.openTime = int(json[0])
        self.open = float(json[1])
        self.high = float(json[2])
        self.low = float(json[3])
        self.close = float(json[4])
        self.volume = float(json[5])
        self.closeTime = int(json[6])
        self.quoteAssetVolume = float(json[7])
        self.numberOfTrade = int(json[8])
        self.takerBuyBaseAssetVolume = float(json[9])
        self.takerBuyQuoteAssetVolume = float(json[10])
        self.canBeIgnored = float(json[11])

    def toArray(self):
        data = [
            self.openTime,
            self.open,
            self.high,
            self.low,
            self.close,
            self.volume,
            self.closeTime,
            self.quoteAssetVolume,
            self.numberOfTrade,
            self.takerBuyBaseAssetVolume,
            self.takerBuyQuoteAssetVolume,
            self.canBeIgnored
        ]

        return data


class BinanceClient:
    def __init__(self):
        self.settings = Settings()
        self.client = Client(self.settings.api_key, self.settings.api_secret)

    def __makeOhlcList(self, ohlcv):
        ohlcList = []
        length = len(ohlcv)
        for i in range(length):
            ohlcJson = ohlcv[(length - 1) - i]

            # parse json
            ohlc = Ohlc(ohlcJson)
            ohlcList.append(ohlc)

        return ohlcList

    # millisecond
    def getServerTime(self):
        serverTime = self.client.get_server_time()
        return long(serverTime["serverTime"])

    def getOhlcList(self, symbol):
        today = self.getServerTime()
        ninetyDaysAgo = today - dayToMillisecond(3 * 30)

        # print(datetime.datetime.now(timezone.utc))
        #print(datetime.datetime.fromtimestamp(today))
        #print(datetime.datetime.fromtimestamp(ninetyDaysAgo))

        ohlcv = self.client.get_historical_klines(symbol, Client.KLINE_INTERVAL_2HOUR, str(ninetyDaysAgo), str(today))
        ohlcList = self.__makeOhlcList(ohlcv)
        return ohlcList

    def getSymbolList(self):
        jsonObj = self.client.get_symbol_ticker()
        # print(jsonObj[0])
        symbolList = []
        for i in range(len(jsonObj)):
            data = jsonObj[i]
            symbol = data["symbol"]
            # print(symbol)
            if(symbol.find("BTC") > 0):
                symbolList.append(symbol)

        return symbolList


if __name__ == "__main__":
    bc = BinanceClient()
    symbolList = bc.getSymbolList()
    print(len(symbolList))
