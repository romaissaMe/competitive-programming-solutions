class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        not_root = set()
        result=set()
        for e in edges:
            not_root.add(e[1])

        for e in edges:
            if e[0] not in not_root:
                result.add(e[0])
        
        return result


        