class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        if needle == "":
            return 0
        
        elif len(haystack) >= len(needle):
            if needle[0] not in haystack:
                return -1
            
            elif needle in haystack:
                return haystack.index(needle)
            
            else:
                return -1
        else:
            return -1