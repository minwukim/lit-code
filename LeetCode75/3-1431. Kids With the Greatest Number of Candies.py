class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        max_candies = max(candies)
        for x in candies:
            result.append(x+extraCandies>=max_candies)
        return result

        # There should be a smarter way..
        # Possible improvement: max requires sorting, which is O(nlog(n)). 
        # How would I do it with O(n)? Is it possible?
        # Ans: No. 결국 max를 알아야 함. 그리고 max는 O(nlog(n)). 고로 이게 최선임. 


