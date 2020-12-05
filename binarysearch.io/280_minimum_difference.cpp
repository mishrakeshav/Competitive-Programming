int solve(vector<int>& lst1, vector<int>& lst2) {
    sort(lst1.begin(),lst1.end());
    sort(lst2.begin(),lst2.end());
    int i , j;
    i = j = 0;
    int diff = INT_MAX;
    while(i < lst1.size() && j < lst2.size()){
        diff = min(abs(lst1[i]-lst2[j]),diff);
        if(lst1[i] < lst2[j]) i++;
        else if(lst1[i] > lst2[j]) j++;
        else return diff;
    }
    return diff;
}