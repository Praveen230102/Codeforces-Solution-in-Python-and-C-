#include<iostream>
#include<cmath>
using namespace std;
int main(){
	int n, m;
	cin >> n;
	cin >> m;
	int temp;
	temp = pow(2, n);
	cout << m%temp;
}
