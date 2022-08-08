def maxSum_2(array, window_size):

    array_size = len(array)
    triples = {}
    for i in range(array_size - window_size + 1):
        triples[i] = sum(array[i:i+window_size])
    return max(triples.values())
array = [80, -50, 90, 100, 45, 59, 72, 21, 35, 46, 12]
k = 2
answer = maxSum_2(array, k)
print(answer)