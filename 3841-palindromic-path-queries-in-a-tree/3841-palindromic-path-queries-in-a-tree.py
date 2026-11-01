class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def _add(self, idx, val):
        idx += 1
        while idx <= self.n + 1:
            self.tree[idx] ^= val
            idx += idx & (-idx)

    def update_range(self, l, r, val):
        self._add(l, val)
        self._add(r + 1, val)

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res ^= self.tree[idx]
            idx -= idx & (-idx)
        return res


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # 1. Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. Precompute LCA (Binary Lifting) and Euler Tour
        LOG = n.bit_length()
        up = [[0] * LOG for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        initial_P = [0] * n
        timer = 0

        # Iterative DFS to avoid stack overflow in deep trees
        stack = [(0, -1, 0, 1)] # (node, parent, state: 0 for enter / 1 for exit, mask_acc)
        initial_P[0] = 1 << (ord(s[0]) - ord('a'))
        
        # Standard recursive-to-iterative DFS conversion
        # To make it simpler, let's just do standard DFS traversal state
        stack = [0]
        visited = [False] * n
        parent = [-1] * n
        order = []
        
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                order.append(u)
                tin[u] = timer
                timer += 1
                for v in adj[u]:
                    if v != parent[u]:
                        parent[v] = u
                        depth[v] = depth[u] + 1
                        initial_P[v] = initial_P[u] ^ (1 << (ord(s[v]) - ord('a')))
                        stack.append(v)
        
        # Post-visit processing for tout
        for u in reversed(order):
            max_tout = tin[u]
            for v in adj[u]:
                if v != parent[u]:
                    max_tout = max(max_tout, tout[v])
            tout[u] = max_tout

        # Fill binary lifting table
        for u in range(n):
            up[u][0] = parent[u] if parent[u] != -1 else u
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        # 3. Process Queries
        bit = BIT(n)
        current_chars = list(s)
        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                old_c = current_chars[u]
                if old_c != c:
                    delta = (1 << (ord(old_c) - ord('a'))) ^ (1 << (ord(c) - ord('a')))
                    bit.update_range(tin[u], tout[u], delta)
                    current_chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                pu = initial_P[u] ^ bit.query(tin[u])
                pv = initial_P[v] ^ bit.query(tin[v])
                lca_mask = 1 << (ord(current_chars[lca]) - ord('a'))
                
                path_mask = pu ^ pv ^ lca_mask
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)

        return ans
