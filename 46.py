class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ret = []
        def calc_permute(visited:set, path:List[int]) -> None:
            if len(path) >= len(nums):
                ret.append(path.copy())
                return
            for i in range(len(nums)):
                if i in visited:
                    continue 
                visited.add(i)
                path.append(nums[i])
                calc_permute(visited, path)
                path.pop()
                visited.remove(i)
        calc_permute(set(), [])
        return ret
