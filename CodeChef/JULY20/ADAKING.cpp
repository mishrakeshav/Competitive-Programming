#include <iostream>
using namespace std;
typedef long long ll;

int main(){
    int t,k;
    cin >> t;
    while(t--){
        cin >> k;
        int flag = 1;
        int count = 64 - k;
        for(int i=0; i<8; i++){
            for(int j = 0; j < 8; j++){
                if(count > 0){
                    cout << "X";
                    count--;
                }
                else if (flag){
                    cout << "O";
                    flag = 0;
                }
                else{
                    cout << ".";
                }
            }
            cout << "\n";
        }
    }
}