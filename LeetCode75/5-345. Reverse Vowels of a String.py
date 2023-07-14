class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. 모음 위치 파악 (인덱스와 알파벳 자체) -> 딕셔러니 혹은 2d 리스트
        # 2. 프린트
        # 이런 경우 두 번 횡단함. 
        # 그럼 한 번은 가능한가? -> 가능. 뒤 위치를 알아야 놓을 수 있음. 그럼 투 포인터
        vowels = 'AEIOUaeiou'
        s = list(s)
        l,r = 0, len(s)-1
        while l<r:
            while s[l] not in vowels and l<r:
                l = l + 1
            while s[r] not in vowels and l<r:
                r = r - 1
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        return ''.join(s)

        