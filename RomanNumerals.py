from sys import argv

class Numeral:
"""
   Program that take a command line arguement between
   1 and 3999, and converts it to Roman Numerals
"""
    def __init__(self):
        "Initialize list/array of Roman Numerals"
        self.numerals = [
                         ["","I","II","III","IV","V","VI","VII","VIII","IX"],
                         ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
                         ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
                         ["","M","MM","MMM"]
                        ]
        self.range_error = "Error: Number out of range!"

    def convert(self, num):
        "Converts an int to a Roman Numeral"
        roman = ""
        if len(str(num)) > 4 or num >= 4000:
            return self.range_error 
        else:
            for i in range(len(str(num))):
                roman += self.numerals[len(str(num)) - (i+1)][int(str(num)[i])]
        return roman


def main(x):
    n = Numeral()
    print(n.convert(int(x)))

if __name__ == "__main__":
    main(argv[1])

