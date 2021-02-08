class Solution:
    def largestAltitude(self,gain:list[int])->int:
        a=0
        b=0

        for x in gain:
            a+=x
            b=max(a,b)
        return b