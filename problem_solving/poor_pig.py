def poorPigs( buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    time=(minutesToTest//minutesToDie)+1
    count=0
    total=1
    while total < buckets:
        total*=time
        count+=1
    return count



print(poorPigs(4,15,30))