#include <stdio.h>

int main()
{
    int n, product;
    printf("Enter the number whose table you want to know.\n");
    scanf("%d",&n);
    for (int i=1;i<=10;i++)
    {
        product = n*i;
        printf("%d X %d = %d\n",n,i,product);
    }
    return 0;
}
