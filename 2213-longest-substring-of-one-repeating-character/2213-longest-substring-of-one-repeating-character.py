class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int], ) -> list[int]:
        n = len(s)
        # Flattened Segment Tree Arrays to avoid object overhead
        # Size 4 * n is standard for array-based segment trees
        tree_size = 4 * n
        
        pref_len = [0] * tree_size
        suff_len = [0] * tree_size
        max_len = [0] * tree_size
        char_left = [""] * tree_size
        char_right = [""] * tree_size

        # Internal helper to merge left child and right child into a parent node index
        def push_up(node_idx: int, left_child: int, right_child: int, left_len: int, right_len: int):
            char_left[node_idx] = char_left[left_child]
            char_right[node_idx] = char_right[right_child]
            
            # 1. Calculate parent prefix length
            p_pref = pref_len[left_child]
            if p_pref == left_len and char_left[left_child] == char_left[right_child]:
                p_pref += pref_len[right_child]
            pref_len[node_idx] = p_pref
            
            # 2. Calculate parent suffix length
            p_suff = suff_len[right_child]
            if p_suff == right_len and char_right[right_child] == char_right[left_child]:
                p_suff += suff_len[left_child]
            suff_len[node_idx] = p_suff
            
            # 3. Calculate base max length
            m_len = max(max_len[left_child], max_len[right_child])
            
            # 4. Middle Check: If borders match, they bridge into a longer sequence
            if char_right[left_child] == char_left[right_child]:
                m_len = max(m_len, suff_len[left_child] + pref_len[right_child])
                
            max_len[node_idx] = m_len

        # Build the segment tree out of the initial string
        def build(node_idx: int, start: int, end: int):
            if start == end:
                pref_len[node_idx] = 1
                suff_len[node_idx] = 1
                max_len[node_idx] = 1
                char_left[node_idx] = s[start]
                char_right[node_idx] = s[start]
                return
            
            mid = (start + end) // 2
            left_child = 2 * node_idx
            right_child = 2 * node_idx + 1
            
            build(left_child, start, mid)
            build(right_child, mid + 1, end)
            
            push_up(node_idx, left_child, right_child, mid - start + 1, end - mid)

        # Update a character in the segment tree
        def update(node_idx: int, start: int, end: int, target_idx: int, val: str):
            if start == end:
                char_left[node_idx] = val
                char_right[node_idx] = val
                # Length stays 1 because it's a single character leaf
                return
            
            mid = (start + end) // 2
            left_child = 2 * node_idx
            right_child = 2 * node_idx + 1
            
            if target_idx <= mid:
                update(left_child, start, mid, target_idx, val)
            else:
                update(right_child, mid + 1, end, target_idx, val)
                
            push_up(node_idx, left_child, right_child, mid - start + 1, end - mid)

        # 1. Build the tree structure initially
        build(1, 0, n - 1)
        
        # 2. Loop through every query and record responses
        result = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            char = queryCharacters[i]
            
            update(1, 0, n - 1, idx, char)
            # The top root node (index 1) always tracks the overall string maximum
            result.append(max_len[1])
            
        return result
