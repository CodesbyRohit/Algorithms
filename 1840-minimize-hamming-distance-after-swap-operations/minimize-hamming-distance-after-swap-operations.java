import java.util.*;

class Solution {
    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int n = source.length;

        // DSU
        int[] parent = new int[n];
        int[] rank = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int[] swap : allowedSwaps) {
            union(swap[0], swap[1], parent, rank);
        }

        // value -> frequency of source values in each component
        Map<Integer, Map<Integer, Integer>> groups = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int root = find(i, parent);

            groups
                .computeIfAbsent(root, k -> new HashMap<>())
                .merge(source[i], 1, Integer::sum);
        }

        int answer = 0;

        // Try to match target[i] with a source value
        // from the same connected component.
        for (int i = 0; i < n; i++) {
            int root = find(i, parent);

            Map<Integer, Integer> freq = groups.get(root);
            int count = freq.getOrDefault(target[i], 0);

            if (count > 0) {
                freq.put(target[i], count - 1);
            } else {
                answer++;
            }
        }

        return answer;
    }

    private int find(int x, int[] parent) {
        if (parent[x] != x) {
            parent[x] = find(parent[x], parent);
        }
        return parent[x];
    }

    private void union(int a, int b, int[] parent, int[] rank) {
        int rootA = find(a, parent);
        int rootB = find(b, parent);

        if (rootA == rootB) {
            return;
        }

        if (rank[rootA] < rank[rootB]) {
            parent[rootA] = rootB;
        } else if (rank[rootA] > rank[rootB]) {
            parent[rootB] = rootA;
        } else {
            parent[rootB] = rootA;
            rank[rootA]++;
        }
    }
}