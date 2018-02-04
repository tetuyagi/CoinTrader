# coding: utf-8
from poloniex import Poloniex, PoloniexPublic

from datetime import datetime, timedelta
import pytz


def to_timestamp(dt):
    timestamp = (dt.replace(tzinfo=pytz.utc) - datetime(1970,1,1, tzinfo=pytz.utc)).total_seconds()
    return int(timestamp)

"""chart data
{
    'date': 1517652000,
    'high': 0.10744064,
    'low': 0.1058018,
    'open': 0.10644509,
    'close': 0.10649979,
    'volume': 218.92080172,
    'quoteVolume': 2055.33133219,
    'weightedAverage: 0.10651363
}
"""

class PoloniexClient:
    def __init__(self):
        self.private_client = Poloniex()
        self.public_client = PoloniexPublic()

        start = datetime.now() - timedelta(days=30)
        end = datetime.now()


        
        res = self.public_client.returnChartData('BTC_ETH', 7200, start, end)
        print(res)




if __name__ == "__main__":
    client = PoloniexClient()

