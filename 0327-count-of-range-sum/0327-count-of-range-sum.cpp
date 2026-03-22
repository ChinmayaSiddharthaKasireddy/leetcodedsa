class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);

        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        return mergeSort(prefix, 0, n + 1, lower, upper);
    }

    int mergeSort(vector<long long>& prefix, int left, int right, int lower, int upper) {
        if (right - left <= 1) return 0;

        int mid = (left + right) / 2;
        int count = mergeSort(prefix, left, mid, lower, upper) +
                    mergeSort(prefix, mid, right, lower, upper);

        int j = mid, k = mid, t = mid;
        vector<long long> temp;

        for (int i = left; i < mid; i++) {
            while (k < right && prefix[k] - prefix[i] < lower) k++;
            while (j < right && prefix[j] - prefix[i] <= upper) j++;
            count += (j - k);
        }

        // merge step
        int i = left;
        while (i < mid && t < right) {
            if (prefix[i] <= prefix[t]) {
                temp.push_back(prefix[i++]);
            } else {
                temp.push_back(prefix[t++]);
            }
        }

        while (i < mid) temp.push_back(prefix[i++]);
        while (t < right) temp.push_back(prefix[t++]);

        for (int i = 0; i < temp.size(); i++) {
            prefix[left + i] = temp[i];
        }

        return count;
    }
};