from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        freq = Counter(s)

        buckets = [[] for _ in range(len(s) + 1)]

        for ch, count in freq.items():
            buckets[count].append(ch)

        result = ""

        for count in range(len(buckets) - 1, 0, -1):
            for ch in buckets[count]:
                result += ch * count

        return result
