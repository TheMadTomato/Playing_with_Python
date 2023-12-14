import Num2Num

def main():
    num = Num2Num.Num2Num(100)
    print("Num2Num object:", num)

    # Test dec2* functions
    print("Decimal to binary:", num.dec2Bin(100))
    print("Decimal to octal:", num.dec2Oct(100))
    print("Decimal to hexadecimal:", num.dec2Hex(100))

    # Test bin2* functions
    print("Binary to decimal:", num.bin2Dec('1100100'))
    print("Binary to octal:", num.bin2Oct('1100100'))
    print("Binary to hexadecimal:", num.bin2Hex('1100100'))

    # Test hex2* functions
    print("Hexadecimal to decimal:", num.hex2Dec('64'))
    print("Hexadecimal to binary:", num.hex2Bin('64'))
    print("Hexadecimal to octal:", num.hex2Oct('64'))

    # Test oct2* functions
    print("Octal to decimal:", num.oct2Dec('144'))
    print("Octal to binary:", num.oct2Bin('144'))
    print("Octal to hexadecimal:", num.oct2Hex('144'))

main()