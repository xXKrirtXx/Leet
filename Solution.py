class Solution:
    #1768
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        x = 0

        while (max(len(word1), len(word2)) > x):
            if (len(word1) > x):
                res += word1[x]
            if (len(word2) > x):
                res += word2[x]
            x += 1

        return res

    #1071
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd
        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1), len(str2))]
        else:
            return ""
    #1431
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result

