# What is the minimum number of boats to carry every person? A boat has a kilogram limit.
# for example if a boat cancarry at most 3 kg, the people should be totaly at most 3 kg

def numRescueBoats(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boats_number = 0
    while left <= right:
        if left == right:
            boats_number += 1
            break
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats_number += 1
    return boats_number


