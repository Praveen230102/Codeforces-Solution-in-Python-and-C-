#include<bits/stdc++.h>
using namespace std;
int main(){
	int a, b, c, total = 7, lemon = 1, app = 2, p = 4;
	cin >> a;
	cin >> b;
	cin >> c;
	for (int i=1;i<=1000000000;i++){
		if ((a < lemon*i) or (b < app*i) or (c < p*i)){
			cout << total*(i-1);
			break;
		}
	}
}
