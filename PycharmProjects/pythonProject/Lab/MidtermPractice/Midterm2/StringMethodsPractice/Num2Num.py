class Num2Num:
    def __init__(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    # methods
    ## 1. dec2Hex
    def toHexChar(self, hexValue):
        if 0 <= hexValue <= 9:
            return chr(hexValue + ord('0'))
        else: # 10 <= hexValue <= 15
            return chr(hexValue - 10 + ord('A'))
    def dec2Hex(self, num):
        hex = ""
        while num != 0:
            hexValue = num % 16
            hex = self.toHexChar(hexValue) + hex
            num = num // 16
        return hex

    def hex2Dec(self, hexString):
        decimalValue = 0
        for i in range(len(hexString)):
            ch = hexString[i].upper()
            if 'A' <= ch <= 'F' or '0' <= ch <= '9':
                decimalValue = decimalValue * 16 + (ord(ch) - ord('A') + 10)
            else:
                return 0
        return decimalValue

    ## 2. dec2Bin
    def dec2Bin(self, num):
        bin = ""
        while num != 0:
            binValue = num % 2
            bin = str(binValue) + bin
            num = num // 2
        return bin
    def bin2Dec(self, binString):
        decimalValue = 0
        for i in range(len(str(binString))):
            ch = binString[i]
            if ch == '0' or ch == '1':
                decimalValue = decimalValue * 2 + (ord(ch) - ord('0'))
            else:
                return -1
        return decimalValue

    ## 3. dec2Oct
    def dec2Oct(self, num):
        oct = ""
        while num != 0:
            octValue = num % 8
            oct = str(octValue) + oct
            num = num // 8
        return oct
    def oct2Dec(self, octString):
        decimalValue = 0
        for i in range(len(octString)):
            ch = octString[i]
            if '0' <= ch <= '7':
                decimalValue = decimalValue * 8 + (ord(ch) - ord('0'))
            else:
                return -1
        return decimalValue

    ## 4. bin2Hex
    def bin2Hex(self, binString):
        hex = ""
        while len(binString) % 4 != 0:
            binString = '0' + binString
        for i in range(0, len(binString), 4):
            fourBits = binString[i:i+4]
            hexValue = self.bin2Dec(fourBits)
            hex += self.toHexChar(hexValue)
        return hex
    def hex2Bin(self, hexString):
        bin = ""
        for i in range(len(hexString)):
            ch = hexString[i]
            if 'A' <= ch <= 'F' or '0' <= ch <= '9':
                bin += self.dec2Bin(self.hex2Dec(ch))
            else:
                return -1
        return bin

    ## 5. bin2Oct
    def bin2Oct(self, binString):
        oct = ""
        while len(binString) % 3 != 0:
            binString = '0' + binString
        for i in range(0, len(binString), 3):
            threeBits = binString[i:i+3]
            octValue = self.bin2Dec(threeBits)
            oct += str(octValue)
        return oct
    def oct2Bin(self, octString):
        bin = ""
        for i in range(len(octString)):
            ch = octString[i]
            if '0' <= ch <= '7':
                bin += self.dec2Bin(self.oct2Dec(ch))
            else:
                return -1
        return bin

    ## 6. hex2Oct
    def hex2Oct(self, hexString):
        oct = ""
        for i in range(len(hexString)):
            ch = hexString[i]
            if 'A' <= ch <= 'F' or '0' <= ch <= '9':
                oct += self.dec2Oct(self.hex2Dec(ch))
            else:
                return -1
        return oct
    def oct2Hex(self, octString):
        hex = ""
        for i in range(len(octString)):
            ch = octString[i]
            if '0' <= ch <= '7':
                hex += self.dec2Hex(self.oct2Dec(ch))
            else:
                return -1
        return hex

    def __repr__(self):
        return "Num2Num(" + str(self.__num) + ")"
    def __str__(self):
        return "Num2Num(" + str(self.__num) + ")"