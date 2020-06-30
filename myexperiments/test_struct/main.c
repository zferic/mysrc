#include <stdio.h>

int main(){
	int a[10];
	typedef struct sic_struct {
		int x;
		char y;
		int* ptr;
	} sic;
	printf("%d\n",a[0]);
	sic b[5];
	printf("%p\n",b[0]);
	return 0;
}

