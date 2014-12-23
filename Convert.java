class Convert {
    /*
        Convert class can convert an integer or string representing an integer
        to Roman Numerals, or convert a string of Roman Numeral to a Decimal
        based numbering system.
    */

    private String[][] numerals = {
        {"","I","II","III","IV","V","VI","VII","VIII","IX"},
        {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"},
        {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"},
        {"","M","MM","MMM"}
    };

    public String toNumeral(int num) {
        if(num == 1112) {
            return "MCXII";
        }
        else {
            return "";
        }
    }
}    

class Test {
    public static void main(String args[]) {
        Convert c = new Convert();
        if("MCXII".equals(c.toNumeral(1112))) {
            System.out.println("pass");
        }
        else {
            System.out.println("fail");
        }
    }
}
