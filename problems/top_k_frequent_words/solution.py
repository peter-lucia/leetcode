class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """

        :param words:
        :param k:
        :return:
        """

        words.sort()
        words_set = set(words)
        lookup = {}
        for word in words_set:
            lookup[word] = 0

        for word in words:
            lookup[word] += 1

        tuples = [(key, value) for key,value in lookup.items()]
        tuples = sorted(tuples, key=lambda val: (-val[1], val[0]))

        result = []
        for i in range(k):
            result.append(tuples[i][0])
        return result
