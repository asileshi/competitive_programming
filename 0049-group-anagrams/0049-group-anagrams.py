class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for i in strs:
            temp = "".join(sorted(i))
            
            ana[temp].append(i)
        ans = []
        for i in ana:
            ans.append(ana[i])
        return ans