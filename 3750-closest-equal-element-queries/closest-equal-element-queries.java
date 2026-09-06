import java.util.*;

class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        int n = nums.length;

        Map<Integer, List<Integer>> map = new HashMap<>();

        // Store indices of each value
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }

        List<Integer> answer = new ArrayList<>();

        for (int query : queries) {
            List<Integer> list = map.get(nums[query]);

            // No other occurrence
            if (list.size() == 1) {
                answer.add(-1);
                continue;
            }

            // Position of query inside the occurrence list
            int pos = Collections.binarySearch(list, query);

            int size = list.size();

            // Previous and next occurrence
            int prev = list.get((pos - 1 + size) % size);
            int next = list.get((pos + 1) % size);

            int distPrev = Math.abs(query - prev);
            distPrev = Math.min(distPrev, n - distPrev);

            int distNext = Math.abs(query - next);
            distNext = Math.min(distNext, n - distNext);

            answer.add(Math.min(distPrev, distNext));
        }

        return answer;
    }
}