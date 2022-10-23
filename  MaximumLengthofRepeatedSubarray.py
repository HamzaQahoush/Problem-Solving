def findLength(nums1, nums2) -> int:
    res=0
    N1=len(nums1)
    N2= len(nums2)
    for i in range (N1):
        for j in range(N2):
            k=0
            while (i+k) < N1 and (j+k) <N2 and  nums1[i+k]== nums2[j+k] :
                k+=1
            res=max(k,res)
        
        return res
        

nums1 = [0,1,1,1,1]

nums2 = [1,0,1,0,1]


print(findLength(nums1, nums2))