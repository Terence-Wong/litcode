from collections import defaultdict
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = [0]*10
        b = [0]*10
        bull = 0
        cow = 0
        for x, y in zip(secret, guess):
            if x == y:
                bull += 1
            else:
                if b[int(x)] > 0:
                    cow += 1
                    b[int(x)] -= 1
                else:
                    a[int(x)] += 1

                if a[int(y)] > 0:
                    cow +=1
                    a[int(y)] -= 1
                else:
                    b[int(y)] += 1

        return str(bull) + "A" + str(cow) + "B"

