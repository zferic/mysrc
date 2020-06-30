#include <stdio.h>
#include <stdlib.h>

void func(int** a){
	*a=malloc(4*sizeof(int));
}

void func2(int** a){
	int* b=*a; /* make *a points b */
	b=malloc(4*sizeof(int));
}

/* This function is to change a*/
int main(){
	int *a=NULL;
	printf("%p\n",a);

	//func(&a);

	func2(&a);

	printf("%p\n",a);
	return 0;
}
