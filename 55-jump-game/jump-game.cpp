class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.size()==1) return true;
        int jump_possible=nums[0];
        if(jump_possible==0) return false;
        for(int i=1;i<nums.size();i++){
            jump_possible--;
            if(nums[i]>jump_possible) jump_possible=nums[i];
            if(jump_possible==0 && i!=nums.size()-1) return false;
        }
        return true;
    }
};