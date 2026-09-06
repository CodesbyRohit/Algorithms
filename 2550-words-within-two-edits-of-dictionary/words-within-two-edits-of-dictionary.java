import java.util.*;

class Solution {
    public List<String> twoEditWords(String[] queries, String[] dictionary) {
        List<String> answer = new ArrayList<>();

        for (String query : queries) {
            for (String word : dictionary) {
                int differences = 0;

                for (int i = 0; i < query.length(); i++) {
                    if (query.charAt(i) != word.charAt(i)) {
                        differences++;

                        if (differences > 2) {
                            break;
                        }
                    }
                }

                if (differences <= 2) {
                    answer.add(query);
                    break;
                }
            }
        }

        return answer;
    }
}