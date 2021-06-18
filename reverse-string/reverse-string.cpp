class Solution {
public:
    void reverseString(vector<char>& s) {
        int length = s.size();
        int left = 0;
        int right = (length-1);
        
        while(left <= right){
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
};