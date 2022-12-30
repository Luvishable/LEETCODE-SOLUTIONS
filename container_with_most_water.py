"""
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

def maxWater(lines):
    left = 0
    right = 1
    areas = []
    while left < len(lines) - 1:
        max_area = 0
        while right < len(lines):
            height = min(lines[left], lines[right])
            width = right - left
            current_area = height * width
            if current_area > max_area:
                max_area = current_area
                areas.append(current_area)
            right += 1
        left += 1
    return max(areas)

array = [5, 9, 2, 1, 4]
print(maxWater(array))
