def mirrorReflection( p: int, q: int) -> int:
    while p % 2 == 0 and q % 2 == 0:
        p //=2
        q //=2

    if q % 2 == 0 :
        return 0
    elif p % 2 == 0:
        return 2
    else:
        return 1

print(mirrorReflection(4,2))

"""
https://leetcode.com/problems/mirror-reflection/
"""