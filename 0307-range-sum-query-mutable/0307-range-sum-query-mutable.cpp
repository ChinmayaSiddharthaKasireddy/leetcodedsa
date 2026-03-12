class NumArray {
private:
    vector<int> bit;
    vector<int> arr;
    int n;

    void add(int index, int val) {
        index++;
        while (index <= n) {
            bit[index] += val;
            index += index & (-index);
        }
    }

    int prefixSum(int index) {
        index++;
        int sum = 0;
        while (index > 0) {
            sum += bit[index];
            index -= index & (-index);
        }
        return sum;
    }

public:
    NumArray(vector<int>& nums) {
        n = nums.size();
        arr = nums;
        bit.resize(n + 1, 0);

        for (int i = 0; i < n; i++)
            add(i, nums[i]);
    }

    void update(int index, int val) {
        int diff = val - arr[index];
        arr[index] = val;
        add(index, diff);
    }

    int sumRange(int left, int right) {
        return prefixSum(right) - prefixSum(left - 1);
    }
};