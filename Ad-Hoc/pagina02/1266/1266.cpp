#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,z,s,i,p,j;
    while(1){
    scanf("%d",&t);
    if(t == 0){
        break;
    }
     z = 0;
     s = 0;
     i = 0;
     p = 0;
     for(j = 0; j < t; j++){
      scanf("%d",&n);
      if(n == 0 && i == 0){
        z++;
        p++;
      }
      else if(n == 0 && i == 1){
        p++;
      }
      if(n == 1){
        i = 1;
        s=s+p/2;
        p= 0;
      }
    }
    if(p > 0){
        s=s-z/2;
        p=p+z;
        s=s+p/2;
    }
    printf("%d\n",s);
  }
   return 0;
}