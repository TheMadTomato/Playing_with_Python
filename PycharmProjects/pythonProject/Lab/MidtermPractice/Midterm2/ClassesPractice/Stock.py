"""
(The Stock class) Design a class named Stock to represent a company’s stock
that contains:
■ A private string data field named symbol for the stock’s symbol.
■ A private string data field named name for the stock’s name.
■ A private float data field named previousClosingPrice that stores the stock
price for the previous day.
■ A private float data field named currentPrice that stores the stock price for
the current time.
■ A constructor that creates a stock with the specified symbol, name, previous
price, and current price.
■ A get method for returning the stock name.
■ A get method for returning the stock symbol.
■ Get and set methods for getting/setting the stock’s previous price.
■ Get and set methods for getting/setting the stock’s current price.
■ A method named getChangePercent() that returns the percentage changed
from previousClosingPrice to currentPrice.
"""
class Stock:
    def __init__(self, symbol, name, previousClosingPrice = 0, currentPrice = 0):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    # Getters
    def getSymbol(self):
        return self.__symbol
    def getName(self):
        return self.__name
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    def getCurrentPrice(self):
        return self.__currentPrice

    # Setters
    def setPreviousClosingPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice
    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    # methods
    def getChangePercent(self):
        if self.__previousClosingPrice == 0:
            return 0
        else:
            return (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice * 100

# test
stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
print(stock.getSymbol(),":",stock.getName())
print("Previous Closing Price:",stock.getPreviousClosingPrice(),"$")
print("Current Price:",stock.getCurrentPrice(),"$")
print(stock.getChangePercent())