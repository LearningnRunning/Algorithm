class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens =     ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones =     ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        t = num // 1000
        h = (num % 1000) // 100
        te = (num % 100) // 10
        o = num % 10

        return thousands[t] + hundreds[h] + tens[te] + ones[o]
