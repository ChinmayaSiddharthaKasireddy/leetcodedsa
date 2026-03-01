class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        // Step 1: Sort by ending value
        sort(pairs.begin(), pairs.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int count = 0;
        int lastEnd = INT_MIN;
        
        // Step 2: Greedily select pairs
        for (auto& p : pairs) {
            if (p[0] > lastEnd) {
                count++;
                lastEnd = p[1];
            }
        }
        
        return count;
    }
};