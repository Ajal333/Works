#include<stdio.h>

int main(void)
{
	int n,c=0,t=0;
	int z=1;
	printf("Enter a number: ");
	scanf("%d",&n);

	for(int i=1;i<=n/2;i++)
	{
		if(t<=n)
		{
		t = t+i;
		c++;
		}
	}

	for(int i=1;i<=c;i++)
	{
		for(int j=(c-1);j>=i;j--)
		{
			printf(" ");
		}
		
		for(int j=1;j<=i;j++)
		{
			if(z<=n)
			{
			printf("%d ",z);
			}
			z++;
		}
		printf("\n");
	}
	
	return 0;
}
