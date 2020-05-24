#include <bits/stdc++.h>
using namespace std;
int main()
{
int t;
cin>>t;
while(t--) {
int n,count=0,flag=0,sumodd=0,sumeven=0;
cin>>n;
int a[n];
int cut=(n/2)+1;
for(int j=2; j<=n+1; j+=2) {
sumeven+=j;
flag++;
}
for(int i=1; i<=n+1; i+=2) {
if(i==cut) {
continue;
}
else {
count++;
sumodd+=i;
}
}
if(flag==count && sumodd==sumeven)
{
cout<<"YES"<<endl;
for(int j=2; j<=n+1; j+=2)
cout<<j<<" ";
for(int i=1; i<=n+1; i+=2)
 {
if(i==cut)
{
continue;
}
else
cout<<i<<" ";
}
cout<<endl;
}
else
cout<<"NO"<<endl;
}
return 0;
}
