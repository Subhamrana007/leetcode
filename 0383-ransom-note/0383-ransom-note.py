class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def count_occurance(x):
            map = {}
            for ch in x:
                if ch in map:
                    map[ch] += 1
                else:
                    map[ch] = 1
            return map

        r = count_occurance(ransomNote)
        m = count_occurance(magazine)

        for key, value in r.items():
            if (key not in m) or (value > m[key]):
                return False
            
        return True    
        
                

        