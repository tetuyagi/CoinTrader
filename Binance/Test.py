from binance.client import Client
from binance.websockets import BinanceSocketManager

import json


api_key = "ffltNnyKSclwexlhMgu9VGIGCcFfqcov4wA3pBLsDxMiv253OoKu9PNEvnErSGIY"
api_secret = "CDKAajuQfq4Va86degtw2HtLRcpVunaKrlYm20mpfGhjbvFIKl0SvCbpLzgAbvUF"
client = Client(api_key, api_secret, {"verify":False, "timeout":20})

class Peyload:
    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.symbol = ""
        self.aggregateTradeId = 0
        self.price = 0
        self.quantity = 0
        self.firstTradeId = 0
        self.lastTradeId = 0
        self.tradeTime = 0
        self.isMarker = False
        self.flag = False


    @staticmethod
    def parse(jsonText):
        try:
            jsonText = jsonText.replace('\'', '\"')
            jsonText = jsonText.replace('True', 'true')
            jsonText = jsonText.replace('False', 'false')
            print("jsonText : " + (jsonText))

            self = Peyload()

            jsonObj = json.loads(jsonText)

            self.eventType = jsonObj["e"]
            self.eventTime = jsonObj["E"]
            self.symbol = jsonObj["s"]
            self.aggregateTradeId= jsonObj["a"]

            self.price = float(jsonObj["p"]) #誤差大丈夫？

            self.quantity = float(jsonObj["q"]) #10億超える？
            #self.firstTradeId = jsonObj["f"]
            #self.lastTradeId = jsonObj["l"]
            self.tradeTime = jsonObj["T"]
            self.isMarker = jsonObj["m"]
            self.flag = jsonObj["M"]
            
            print("price : " + str(self.price))
            print("parse succeeded")
            return self

        except Exception as e:
            print("parse error : " + str(e))



def process_message(msg):
    if msg['e'] == 'error':
        print("error")
        print(msg)

        # close and restart the socket
        bm.close()

    else:
        print("message type: {}".format(msg['e']))
        print(msg)
        peyload = Peyload.parse(str(msg))



bm = BinanceSocketManager(client)

coin = "BNBBTC"
conn_key = bm.start_trade_socket(coin, process_message)

bm.start() 
