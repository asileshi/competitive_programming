class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        graph = defaultdict(list)
        AllWord = wordList+[beginWord,endWord]
        st = set(wordList)
        for w in AllWord:
            list_word = list(w)
            for i in range(len(list_word)):
                for asc in range(97,123):
                    if list_word[i]!=chr(asc):
                        temp_list = list_word.copy()
                        temp_list[i] = chr(asc)
                        string = ''.join(temp_list)
                        if string in st:
                            graph[w].append(string)

        visited = set([beginWord])
        current_level = [beginWord]
        l = 1
        
        while current_level:
            next_level = []
            for cur in current_level:
                if cur == endWord:
                    return l
                for child in graph[cur]:
                    if child not in visited:
                        visited.add(child)
                        next_level.append(child)
            l+=1
            current_level = next_level
        return 0

                        
                    