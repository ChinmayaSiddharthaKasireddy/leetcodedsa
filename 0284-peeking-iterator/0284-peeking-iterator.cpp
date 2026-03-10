class PeekingIterator : public Iterator {
private:
    int nextElement;
    bool has_next;

public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
        if (Iterator::hasNext()) {
            nextElement = Iterator::next();
            has_next = true;
        } else {
            has_next = false;
        }
	}
	
	int peek() {
        return nextElement;
	}
	
	int next() {
        int res = nextElement;

        if (Iterator::hasNext()) {
            nextElement = Iterator::next();
        } else {
            has_next = false;
        }

        return res;
	}
	
	bool hasNext() const {
        return has_next;
	}
};