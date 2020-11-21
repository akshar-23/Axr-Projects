#include <stdio.h>

void main ()
{
    int n,product=1;
    char s;
    printf("Enter a number whose Factorial you want to find.\n");
    scanf("%d",&n);
    for (int t=1;t<=n;t++)
    {
        product = product*t;
    }
    printf("%d! = %d\n",n,product);
}
