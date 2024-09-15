# floyd: https://github.com/smbanaie/floyd-warshall-python
from math import inf
from itertools import product

def floyd_warshall(n, edge):
    rn = range(n)
    dist = [[inf] * n for i in rn]
    nxt = [[0] * n for i in rn]
    for i in rn:
        dist[i][i] = 0
    for u, v, w in edge:
        dist[u - 1][v - 1] = w
        nxt[u - 1][v - 1] = v - 1
    for k, i, j in product(rn, repeat=3):
        sum_ik_kj = dist[i][k] + dist[k][j]
        if dist[i][j] > sum_ik_kj:
            dist[i][j] = sum_ik_kj
            nxt[i][j] = nxt[i][k]
    print("    pair        dist     path")
    for i, j in product(rn, repeat=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(nxt[path[-1]][j])
            print("%3d → %3d  %4d       %s"
                  % (i + 1, j + 1, dist[i][j],
                     ' → '.join(str(p + 1) for p in path)))

if __name__ == '__main__':
    floyd_warshall(4, [
        [0, 1, 2], [0, 2, 7],
        [1, 2, 4], [1, 3, 8], [1, 4, 5],
        [2, 3, 1], [2, 1, 3], 
        [3, 4, 4], 
        [4, 3, 5]
        ])