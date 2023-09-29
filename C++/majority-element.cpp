class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int majority = 0, counter = 0;

        for (int i = 0; i < nums.size(); i++) {

            if (counter == 0) majority = nums[i];
            nums[i] == majority ? counter++ : counter--;
        }
        return majority;
    }
};