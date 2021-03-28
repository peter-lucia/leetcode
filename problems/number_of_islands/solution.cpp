class Solution {
private:
    vector<vector<char>> grid;
    int rows;
    int cols;
public:

    void explore(const int &i, const int &j) {
        // mark the position as visited by setting it to '0'
        grid[i][j] = '0';

        if (i > 0 && grid[i-1][j] == '1') {
            explore(i-1, j);
        }
        if ( i < (rows - 1) && grid[i+1][j] == '1') {
            explore(i+1, j);
        }
        if (j > 0 && grid[i][j-1] == '1') {
            explore(i, j-1);
        }
        if (j < (cols - 1) && grid[i][j+1] == '1') {
            explore(i, j+1);
        }
        // can't explore anymore
        return;
    }
    int numIslands(vector<vector<char>>& grid) {
        this->grid = grid;
        rows = grid.size();
        if (rows == 0)
            return 0;
        cols = grid[0].size();
        int total_islands = 0;
        // count ones,
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (this->grid[i][j] == '1') {
                    ++total_islands;
                    explore(i, j);
                }
            }
        }

        return total_islands;

    }
};

