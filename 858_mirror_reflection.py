class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
#       if theyre odd its hard to find a gcf but u can if theyre both even (2)
        while p % 2 == 0 and q % 2 == 0:
            q /= 2
            p /= 2
#       once one of them is odd, u can make a decision
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1
#      x - 0 - x
#      |   |   | 
#      2 - 1 - 2
#      |   |   |
#      x - 0 - x        
#               ratio        top right most #
#      like a 2x:1y ratio -> hit 2 
#      like a 1x:2y ratio -> hit 0
#      like a 1x:1y ratio -> hit 1

        