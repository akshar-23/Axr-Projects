#include <stdio.h>
int rev(n)
{
    int r=0;
    while (n!=0)
    {
        r = n%10;
        r = r*10;
        n = n/10;
        r = r+n;
        return r;
    }
}
int main()
{
    int n1, n2, sum;
    printf("Enter Two Numbers\n");
    scanf("%d%d",&n1,&n2);
    sum = rev(n1) + rev(n2);
    printf("\nThe sum is %d\n",sum);
    return 0;
}
