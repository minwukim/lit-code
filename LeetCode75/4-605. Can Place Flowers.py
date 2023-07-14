class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0: return True 
        i = 0
        
        while i < len(flowerbed):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                print("here", i)
                n -= 1
                if n==0: 
                    return True
                i += 1 # 다음 건 볼 필요도 없음.
            i += 1
            print(i)

        return False

        # 주의사항 1: 시작과 꼬리는 (i==0 or flowerbed[i-1]) 이런 식으로 처리. OR는 선후 관계있음. 
        # 주의사항 2: n은 미리 소진 될 수 있음. 그런 경우 바로 깎아버리기.
        # 주의사항 3: 0같은 테스트케이스 면밀히 살필것

# In Python, logical expressions are evaluated from left to right and the evaluation stops as soon as the outcome is known. This principle is known as short-circuit evaluation.
# In the case of the logical or operator, if the first operand is True, then Python doesn't bother evaluating the second operand, because the or operator is True if either of its operands are True.
# Therefore, in your statement (i==0 or flowerbed[i-1]==0), if i is 0, then i==0 is True, and Python doesn't evaluate flowerbed[i-1]==0 at all.


