class Solution {
public:
    int mySqrt(int x) {
       long left,right,mid;
        left = 0;
        right = (long)x + 1;
        while (left < right){
            mid = left + (right-left)/2;
            if(mid*mid > x){
                right = mid;
            }else{
                left = mid + 1;
            }
        } 
        left--;
        return (int)left;
    }
};
