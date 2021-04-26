#include<bits/stdc++.h>
// #include <sys/resource.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;


using namespace std;

int main(){
    // rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    // setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    int tt;
    cin >> tt;
    while(tt--){
        int x , y;
        cin >> x >> y;
        int flag = 0;
        for(int i = 1; i*i <= x+y ; i++){
            if(i*i == x+y){
                flag = 1;
                break;
            }
        }
        if(!flag){
            cout << "NO" << endl;
            continue;
        }
        int n = sqrt(x+y);
        int odd = 1;
        int even = n - 1;
        while(y != 2*odd*even && odd < n and even > 0){
            odd++;
            even--;
        }
        if(odd == n or even == 0 ){
            cout << "NO" << endl;
            continue;
        }
        int root = 1;
        vector<int> level1;
        vector<int> level2;
        int k = 2;
        for(int i = 0; i < odd; i++){
            level1.push_back(k);
            k++;
        }
        for(int i = 0; i < even-1; i++){
            level2.push_back(k);
            k++;
        }
        cout << "YES" << endl;
        cout << level1.size() + level2.size()  + 1 << endl;
        for(int i = 0; i < level1.size(); i++){
            cout << 1 << " " <<level1[i] << endl;
        }
        for(int i = 0; i < level2.size(); i++){
            cout << 2 << " " << level2[i] << endl;
        }

    }
    return (int)0;
}