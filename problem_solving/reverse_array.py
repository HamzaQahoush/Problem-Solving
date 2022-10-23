list1 = [1, 2, 3, 4, 5]



def reverse_arr(list1):
    L=len(list1)
    for i in range(L//2):
        n=list1[i]
        list1[i]=list1[L-i-1]
        list1[L-i-1]=n
    return list1

print(reverse_arr(list1))