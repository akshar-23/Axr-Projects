#include <stdio.h>
#include <string.h>
void main()
{
    char n[100],p[100];
    for(int x=1;x>0;x++)
    {
        printf("Enter your name please.\n");
        gets(n);
        printf("Hello %s !\n",n);
        printf("Please enter your password.\n");
        gets(p);
        if(strcmp(n,"Akshar")==0 && strcmp(p,"Ironman")==0)
        {
            printf("ACCESS GRANTED.\n");
            break;
        }
        else
        {
            printf("ACCESS DENIED. Please try again.\n\n");
        }
    }
}
