
MAX_N = 1000

# 初始化每个节点的父节点
par = [i for i in range(MAX_N)]
# 初始化树的高度
rank = [0 for _ in range(MAX_N)]


def find(x):
    """
    查找根节点
    """
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


def unite(x, y):
    """
    节点合并到同一颗子树
    """
    x = find(x)
    y = find(y)

    # 位于同一颗子树上面，不需要处理
    if x == y:
        return

    # 从rank小的往rank大的合并
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        # y 合并 到 x，所以如果rank相同时，需要把x对应的rank进行更新
        if rank[x] == rank[y]:
            rank[x] += 1


def same(x, y):
    """
    判断两个节点是否在同一颗子树上面
    """
    return find(x) == find(y)
