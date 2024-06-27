class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        print(edges[0][0])
        print(edges[1])
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]
