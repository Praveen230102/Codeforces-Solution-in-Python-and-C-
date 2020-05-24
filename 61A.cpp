#include<iostream>
using namespace std;
int main()
{
	string s1, s2;
	string rem = "";
	cin >> s1;
	cin >> s2;
	for (int i = 0;i<s1.length();i++){
		for (int j = i;j<s2.length();j++){
			if (s1[i] == s2[j]){
				rem += "0";
				break;
			}
			else{
				rem += "1";
				break;
			}
		}
	}
	cout << rem;
}
