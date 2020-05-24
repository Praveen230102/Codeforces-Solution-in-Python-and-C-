#include<bits/stdc++.h>
#define ll long long
using namespace std;

string a,b,c;

int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		cin>>a>>b>>c;
		int n=a.length();
		int flag=1;
		for(int i=0;i<n&&flag;i++)
		{
			if(a[i]!=b[i])
			{
				if(a[i]==c[i]) continue;
				else if(b[i]==c[i]) continue;
				else flag=0;
			}
			else
			{
				if(a[i]!=c[i]) flag=0;
			}
		}
		if(flag) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}
