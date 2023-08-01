# This is the solution using a global scope variable; faster but not very conventional.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def build(i:int, path:List) -> None:
            if len(path) == k:
                ret.append(path.copy())
                return 
            if i>n: return
            build(i+1, path)
            path.append(i)
            build(i+1, path)
            path.pop()
        build(1, [])
        return ret

# Here I have not used a global variable returned evrything in-function;

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def build(i:int, path:list) -> list[list[int]]:
            if len(path) == k:
                return [path.copy()]
            if i>n:
                return []
            not_picked = build(i+1, path)
            path.append(i)
            picked = build(i+1, path)
            path.pop()
            return not_picked + picked
        return build(1, [])