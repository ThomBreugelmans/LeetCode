from functools import reduce


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # basic description, move through string per character, if you find a starting character from a string in words,
        # test if it is an actual substring, if not continue iterating from where you found the character, else
        # if it is a substring, test if the characters afterwards are also substrings, if not, continue from first starting character

        # get starting characters of all words
        ws = {}
        for w in words:
            if w[0] not in ws:
                ws[w[0]] = []
            ws[w[0]].append(w)

        length_of_all_words = reduce(lambda a, b: a + len(b), words, 0)
        indices = set()
        for i in range(len(s)-length_of_all_words+1):
            q = [(i, words)]
            while len(q) > 0:
                start, p_words = q.pop(0)

                if len(p_words) == 0:
                    # we have a substring that has a permutation of all words in 'words'
                    indices.add(start - length_of_all_words)
                    continue

                if start >= len(s) or s[start] not in ws.keys():
                    continue

                p_subs = [w for w in ws[s[start]] if w in p_words]
                max_len = max(map(lambda w: len(w), p_subs), default=0)
                for j in range (max_len):
                    # move through next string from position 'start'
                    # and for each possible substring (str in p_subs) if the chars do not match,
                    # or you reached the end of 's', but not the substring, then remove the substring from p_subs
                    new_subs = p_subs[:]
                    for w in p_subs:
                        if j < len(w) and ((start + j) >= len(s) or s[start + j] != w[j]):
                            new_subs.remove(w)
                    p_subs = new_subs
                # p_subs now only contains words that are a next substring, add those to the queue along with the missing words
                for w in p_subs:
                    new_p_words = p_words[:]
                    new_p_words.remove(w)
                    q.append((start + len(w), new_p_words))

        return sorted(list(indices))
