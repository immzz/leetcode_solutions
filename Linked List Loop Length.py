def answer(numbers):
    # your code here
    visited = [False] * len(numbers)
    n_people = 0
    slow = 0
    fast = 0
    while(True):
        slow = numbers[slow]
        fast = numbers[numbers[fast]]
        if slow == fast:
            break
    
    fast = 0
    while(True):
        slow = numbers[slow]
        fast = numbers[numbers[fast]]
        if slow == fast:
            break
    
    current = slow
    print current
    while(True):
        if visited[current]:
            return n_people
        else:
            visited[current] = True
            current = numbers[current]
    
print answer([1,2,1])
            