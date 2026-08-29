class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;
        int[] sorted = nums.clone();
        Arrays.sort(sorted);

        Map<Integer, Integer> parent = new HashMap<>();
        for(int v : sorted) parent.put(v, v);

        for(int i = 1; i < n; i++){
            if(sorted[i] - sorted[i - 1] <= limit){
                union(parent, sorted[i], sorted[i - 1]);
            }
        }

        Map<Integer, PriorityQueue<Integer>> groups = new HashMap<>();
        for(int v : sorted){
            int root = find(parent, v);
            groups.computeIfAbsent(root, k-> new PriorityQueue<>()).add(v);
        }

        int[] ans = new int[n];
        for(int i = 0; i < n; i++){
            int root = find(parent, nums[i]);
            ans[i] = groups.get(root).poll();
        }
        return ans;
    }
    private int find(Map<Integer, Integer> parent, int x){
        if(parent.get(x) != x){
            parent.put(x, find(parent, parent.get(x)));
        }
        return parent.get(x);
    }
    
    private void union(Map<Integer, Integer> parent, int a, int b){
        int pa = find(parent, a);
        int pb = find(parent, b);
        if(pa != pb) parent.put(pa, pb);
    }
}