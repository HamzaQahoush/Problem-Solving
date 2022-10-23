def solution(numbers):
    res=[]
    
    for i in range(len(numbers)-2):
        for j in range(i+2,len(numbers)):
            if numbers[i] < numbers[j-1] > numbers[j] or   numbers[i] > numbers[j-1] < numbers[j]:
                res.append(1)
                break
            else:
                res.append(0)
                break
    return res
