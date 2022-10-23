def can_cut(ribbons, k, L):
    cut = 0
    for rib in ribbons:
        cut += rib // L
    return cut >= k


def max_ribbon(ribbons, k):
    # ribbons.sort()
    # s=(sum(ribbons)//k )+1
    # while s > s//2 :
    #     rib_c=0
    #     for rib in  ribbons[::-1]:
    #         rib_c += rib//s
    #         if (rib_c) >= k :
    #             return s
    #     s-=1
    # return -1
    l = 1
    r = max(ribbons)
    while l <= r:
        mid = (l + r) // 2

        if can_cut(ribbons, k, mid):
            l = mid + 1
        else:
            r = mid - 1
    return r


ribbons = [5, 2, 7, 4, 9]
# 5
k = 5
print(max_ribbon(ribbons, k))
