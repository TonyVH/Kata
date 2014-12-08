from sys import argv

class Convert:
    """
        Convert class can convert an integer or string representing an integer
        to Roman Numerals, or convert a string of Roman Numeral to a Decimal
        based numbering system.
    """
    def __init__(self):
        "Initialize list/array of Roman Numerals"
        self.numerals = [
                         ["","I","II","III","IV","V","VI","VII","VIII","IX"],
                         ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
                         ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
                         ["","M","MM","MMM"]
                        ]
        self.decimal = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        self.range_error = "Error: Number out of range!"

    def toNumeral(self, num):
        "Converts an int to a Roman Numeral"
        roman_numerals = ""
        if num != str(num):
            num = str(num)
        if len(num) > 4 or int(num) >= 4000:
            return self.range_error 
        else:
            for i in range(len(num)):
                roman_numerals += self.numerals[len(num) - (i+1)][int(num[i])]
        return roman_numerals

    def toDecimal(self, numeral):
        "Takes a Roman Numeral string as an argument"
        total = 0
        if len(numeral) > 1:
            for i in range(len(numeral)-1):
                if self.decimal.get(numeral[i], 0) < self.decimal.get(numeral[i+1], 0):
                    total -= self.decimal.get(numeral[i], 0)
                else:
                    total += self.decimal.get(numeral[i], 0)
            total += self.decimal.get(numeral[-1], 0)
        else:
            total += self.decimal.get(numeral, 0)
        return total 



# Test the program with a command line argument.
def main(x):
    n = Convert()
    print(n.toDecimal(x))

if __name__ == "__main__":
    main(argv[1])

