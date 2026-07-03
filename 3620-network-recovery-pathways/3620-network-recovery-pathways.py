from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            costs.append(w)

        # Topological order
        q = deque(i for i in range(n) if indegree[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        INF = float("inf")

        def can(score):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                for v, w in graph[u]:
                    if w < score:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        if not costs:
            return -1

        lo, hi = min(costs), max(costs)
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans