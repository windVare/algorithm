class Solution:

    def findCircleNum(self, M) -> int:
        parent = [i for i in range(len(M))]
        rank = [0 for _ in range(len(M))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def same(x, y):
            return find(x) == find(y)

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return

            if rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1

        for i in range(len(M)):
            for j in range(len(M[i])):
                if i == j or not M[i][j]:
                    continue
                if same(i, j):
                    continue
                union(i, j)

        # 更新每个节点的根节点
        for i in range(len(M)):
            find(i)
        return len(set(parent))


if __name__ == '__main__':
    # print(Solution().findCircleNum([[1, 1, 0],
    #                                 [1, 1, 0],
    #                                 [0, 0, 1]]))
    # print(Solution().findCircleNum([[1, 1, 0],
    #                                 [1, 1, 1],
    #                                 [0, 1, 1]]))
    print(Solution().findCircleNum(
        [[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]))
