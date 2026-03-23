class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0) return false;
        
        // Check power of 2 and bit position
        return (n & (n - 1)) == 0 && (n & 0x55555555);
    }
};