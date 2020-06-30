#include <stdio.h>

int main() {
	long double a = 5.99999943666;
	printf("i am a float %.11Lf\n",a);
	double b = 5.99999943666;
	printf("i am a float %f\n",b);
	printf("i am a float %.11f\n",b);
	printf("i am a float %g\n",b);
	printf("i am a float %010.8f\n",b);
	return 0;
}