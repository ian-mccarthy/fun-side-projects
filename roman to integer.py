# roman to integer
# Given a roman numeral, convert it to an integer.
# hash map 

class Solution:
    def romanToInt(self, s : str) -> int:
        roman_hash_map = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        res = 0

        for i in range (len(s)):
            if i + 1 < len(s) and roman_hash_map [s[i]] < roman_hash_map [s[i + 1]]:
                res -= roman_hash_map[s[i]]
            else:
                res += roman_hash_map[s[i]]
        
        return res

#examples : "III" "MCMXCIV" "LVIII" "CD"

class_instance = Solution()
result = class_instance.romanToInt ("III")

print (result)

#Given an integer, convert it to roman numeral
#uses nested list
class Solution_2:
    def intToRoman(self, num: int) -> str:
        
        symbolList = [["I", 1],  ["IV", 4], ["V" , 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                      ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        res = ""
        
        for sym, val in reversed(symbolList):
            if num // val:
                count = num // val
                res += (sym * count)
                num = num % val
        return res

int_to_roman_instance = Solution_2()
result_2 = int_to_roman_instance.intToRoman (97)
print (result_2)

