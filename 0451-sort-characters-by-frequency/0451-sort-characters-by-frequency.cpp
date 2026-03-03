class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> freq;
        
        // Step 1: Count frequency
        for (char c : s) {
            freq[c]++;
        }
        
        // Step 2: Store in vector
        vector<pair<char, int>> vec(freq.begin(), freq.end());
        
        // Step 3: Sort by frequency (descending)
        sort(vec.begin(), vec.end(), [](pair<char,int>& a, pair<char,int>& b) {
            return a.second > b.second;
        });
        
        // Step 4: Build result
        string result = "";
        for (auto &p : vec) {
            result.append(p.second, p.first);
        }
        
        return result;
    }
};