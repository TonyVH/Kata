from sys import argv

class Numeral:
    """
        Class that takes an integer or string of numbers between 1 and 3999 
        as an argument, and converts it to Roman Numerals.
        For example: Numeral_object.convert(1234) returns MCCXXXIV
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
        roman_numerals = ""
        if num != str(num):
            num = str(num)
        if len(num) > 4 or int(num) >= 4000:
            return self.range_error 
        else:
            for i in range(len(num)):
                roman_numerals += self.numerals[len(num) - (i+1)][int(num[i])]
        return roman_numerals


# Test the program with a command line argument.
def main(x):
    n = Numeral()
    print(n.convert(x))

if __name__ == "__main__":
    main(argv[1])

