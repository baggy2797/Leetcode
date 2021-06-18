class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
         unordered_map<int,int> mymap;
        for(int i=0;i<nums.size();i++){
            int finder = target - nums[i];
            if(mymap.find(finder)!=mymap.end())
            {
                return {i,mymap[finder]};
            }
            mymap[nums[i]] = i;
        }
        return {};
    }
};