class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        for x in strs:
            sorted_list.append("".join(sorted(x)))
            
        out = []
        visited = [False] * len(strs)
        
        for i in range(len(strs)):
            if visited[i]: 
                continue
                
            current_group = [strs[i]]
            visited[i] = True
            
            for j in range(i + 1, len(strs)):
                if not visited[j] and sorted_list[i] == sorted_list[j]:
                    current_group.append(strs[j])
                    visited[j] = True
                    
            out.append(current_group)
            
        return out