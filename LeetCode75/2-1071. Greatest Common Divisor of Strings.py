from math import gcd
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # 1. Compare the length to obtain shorter and longer
        shorter, longer = str1, str2
        if len(str1) > len(str2):
            shorter = str2
            longer = str1
        
        # 2. Run the while loop to check if divisible
        i = len(shorter)
        while i > 0:
            # 2-1. Check if the length is divisible
            if len(shorter)%i==0 and len(longer)%i==0:
                # 2-2. If so, check if divisible
                divider = shorter[:i]
                if shorter == divider * (len(shorter)/i) and longer == divider * (len(longer)/i):
                    return divider
            i -= 1
        return ""
        
        #################################################
        
        # 문제: 하나하나 깎아 들어가는 것은 다소 멍청함.
        # 해결책: GCD의 특성을 exploit할 것.
        # GCD의 특성: concatenate시 패턴 반복. 앞으로도, 뒤로도 동일함.
        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1),len(str2))]
        return ""


