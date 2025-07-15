class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        map<int,int> mpp;
        for(auto i:nums){
            mpp[i]++;
        }
        vector<int> answer;
        for(auto it:mpp){
            if(it.second==1) answer.push_back(it.first);
        }
        return answer;
    }
};