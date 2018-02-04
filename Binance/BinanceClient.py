# coding: utf-8
from binance.client import Client
from binance.exceptions import BinanceRequestException, BinanceAPIException
from binance.helpers import date_to_milliseconds, interval_to_milliseconds
from settings import Settings
from Helper import dayToMillisecond

import datetime
import re

import time


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
        try:
            serverTime = self.client.get_server_time()
            return int(serverTime["serverTime"])

        except (BinanceRequestException, BinanceAPIException, Exception) as e:
            print("getServerTime error:{}".format(e))
            return None

    def getOhlcList(self, symbol):
        try:
            today = date_to_milliseconds("now UTC")
            # today = self.getServerTime()
            ninetyDaysAgo = today - dayToMillisecond(3 * 30)
            # ninetyDaysAgo = today - dayToMillisecond(30)

            # ohlcv = self.client.get_historical_klines(symbol, Client.KLINE_INTERVAL_2HOUR, str(ninetyDaysAgo), str(today))
            ohlcv = self.get_historical_klines(symbol, Client.KLINE_INTERVAL_2HOUR, str(ninetyDaysAgo), str(today))
            print("len(ohlcv) : {}".format(len(ohlcv)))
            ohlcList = self.__makeOhlcList(ohlcv)

            return ohlcList

        except (BinanceRequestException, BinanceAPIException, Exception) as e:
            print("getOhlcList error:{}".format(e))
            return None


    def getSymbolList(self):
        try:
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

        except (BinanceRequestException, BinanceAPIException, Exception) as e:
            print("getSymbolList error:{}".format(e))
            return None


    def get_historical_klines(self, symbol, interval, start_str, end_str=None):
            # init our list
        output_data = []

        # setup the max limit
        limit = 500

        # convert interval to useful value in seconds
        timeframe = interval_to_milliseconds(interval)

        # convert our date strings to milliseconds
        start_ts = date_to_milliseconds(start_str)

        # if an end time was passed convert it
        end_ts = None
        if end_str:
            end_ts = date_to_milliseconds(end_str)

        idx = 0
        # it can be difficult to know when a symbol was listed on Binance so allow start time to be before list date
        symbol_existed = False
        while True:
            # fetch the klines from start_ts up to max 500 entries or the end_ts if set
            temp_data = self.client.get_klines(
                symbol=symbol,
                interval=interval,
                limit=limit,
                startTime=start_ts,
                endTime=end_ts
            )

            # handle the case where our start date is before the symbol pair listed on Binance
            if not symbol_existed and len(temp_data):
                symbol_existed = True

            if symbol_existed:
                # append this loops data to our output data
                if len(temp_data) == 0:
                    break

                output_data += temp_data

                # update our start timestamp using the last value in the array and add the interval timeframe
                start_ts = temp_data[len(temp_data) - 1][0] + timeframe
            else:
                # it wasn't listed yet, increment our start date
                start_ts += timeframe

            idx += 1
            # check if we received less than the required limit and exit the loop
            if len(temp_data) < limit:
                # exit the while loop
                break

            # sleep after every 3rd call to be kind to the API
            if idx % 3 == 0:
                time.sleep(1)

        return output_data


if __name__ == "__main__":
    bc = BinanceClient()
    symbolList = bc.getSymbolList()
    print(len(symbolList))
