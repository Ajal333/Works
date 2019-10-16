#include<stdio.h>
#include<math.h>

int main(void)
{
	int t=0,s=0;
	double n1,n2;
	double n;
	int z=1;
	printf("Enter a number: ");
	scanf("%le",&n);

	n1=sqrt(n*2*4);
	n2=(1+n1)/2;

	int n3;
	n3=(int)n2;

	for(int i=1;i<=(n3);i++)
	{
		for(int j=(n3-1);j>=i;j--)
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
