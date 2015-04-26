#include <stdio.h>
#define MAX 1000
int main(int argc, char const *argv[]) {
	int i,j;
	long sum=0;
	for(i=1;i<MAX;i++)
		if(i%3==0 || i%5==0)
			sum+=i;
	printf("%ld\n",sum);
	return 0;
}