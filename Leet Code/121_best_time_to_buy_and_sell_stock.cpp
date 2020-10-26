class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()==0) return 0;
        int mx = 0;
        int mi = prices[0];
        for(const auto i:prices){
            mx = max(mx,i-mi);
            mi = min(mi,i);
        }
        return mx;
    }
};