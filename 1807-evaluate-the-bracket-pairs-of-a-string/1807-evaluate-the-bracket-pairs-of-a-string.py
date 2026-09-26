class Solution:
    def evaluate(self, s, knowledge):
        d = dict(knowledge)
        result = ""
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]

                result += d.get(key, "?")
                i = j + 1
            else:
                result += s[i]
                i += 1

        return result
            