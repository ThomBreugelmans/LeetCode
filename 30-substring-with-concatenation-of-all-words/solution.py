class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        for w in words:
            if w not in s:
                return []

        next_permutations = [('', words)]
        indices = []
        while len(next_permutations) > 0:
            p, p_words = next_permutations.pop(0)
            if p in s:
                nextt = self.next_permutations(p, p_words)
                if len(nextt) > 0:
                    for w in nextt:
                        next_words = p_words[:]
                        next_words.remove(w[len(p):])
                        next_permutations.append((w, next_words))
                else:
                    start = 0
                    while p in s[start:]:
                        index = s.find(p, start)
                        indices.append(index)
                        start = index + 1

        return sorted(indices)

    @staticmethod
    def next_permutations(cur_str: str, words: list[str]) -> set[str]:
        next_permutations = set()
        for w in words:
            next_permutations.add(cur_str + w)
        return next_permutations
