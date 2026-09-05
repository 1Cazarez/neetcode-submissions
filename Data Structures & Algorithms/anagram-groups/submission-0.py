class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            alphabet_map = [0]*26
            for char in s:
                alphabet_map[ord(char)- ord('a')] += 1
            key = tuple(alphabet_map)
            groups[key] = groups.get(key,[])+ [s]

        return list(groups.values())