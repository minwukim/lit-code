class Solution(object):
    def mergeAlternately(self, word1, word2):
        # 1. Compare the lengths of two strings and obtain the shorter one
        len1 = len(word1)
        len2 = len(word2)
        shorter, longer = 0,0
        if(len1 <= len2):
            shorter = len1
            longer = len2
        else:
            shorter = len2
            longer = len1
        result=""

        # 2. append the chars alternatively till the index "shorter"
        i=0
        while i<shorter:
            result += word1[i]
            result += word2[i]
            i+=1

        # 3. append the rest
        while i<longer:
            if len1<len2:
                result += word2[i]
            else:
                result += word1[i]
            
            i+=1
        return result

        #################################################
        
        # 문제: 너무 끊어가는 경향이 있음. 어떻게 간결하게 갈 것인가:
        # 정답: 바로 longer로 while loop 돌리고, 그 안에서 컨디셔닝

        result=""
        i = 0
        while i<len(word1) or i<len(word2):
            if i<len(word1):
                result += word1[i]
            if i<len(word2):
                result += word2[i]
            i += 1
        return result
        

