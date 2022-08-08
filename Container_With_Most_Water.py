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