class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // 1. flip along top left to bottom right axis
        // 2. reverse each row


        int n = matrix.size();
        int m = matrix[0].size();

        for (int i = 0; i < n; i++) {
            for (int j = i; j < m; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }

        for (int i = 0; i < n; i++) {
            // reverse the row
            for (int j = 0; j < int(n / 2); j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][m-j-1];
                matrix[i][m-j-1] = tmp;
            }
        }
        
    }
};
