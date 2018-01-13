from coincheck import order, market, account



m1 = market.Market()
print("ticker : " + str(m1.ticker()) + "\n")

print("trades : " + str(m1.trades()) + "\n")

print("orderbooks : " + str(m1.orderbooks()) + "\n")


