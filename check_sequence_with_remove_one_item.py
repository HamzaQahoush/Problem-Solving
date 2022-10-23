

def check_ascending(nums):
    return all(a<b for a,b in zip(nums, nums[1:]))

def solution(sequence):
    removed = 0
    previous_maximum = maximum = float('-infinity')
    for s in sequence:
        if s > maximum:
            # All good
            previous_maximum = maximum
            maximum = s
        elif s > previous_maximum:
            # Violation - remove current maximum outlier
            removed += 1
            maximum = s
        else:
            # Violation - remove current item outlier
            removed += 1
        if removed > 1:
            return False
    return True
    
sequence=  [1, 3, 2, 1]

print(solution(sequence))