class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = collections.deque()
        queue.append((beginWord,1))
        wordLength = len(beginWord)
        while queue:
            word,step = queue.popleft()
            if word == endWord:
                return step
            for i in range(wordLength):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c +word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord,step+1))
        return 0
        