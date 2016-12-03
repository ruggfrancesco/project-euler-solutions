#include <stdio.h>

int main() {

	int a, b, x, y, ab, xy, prod = 2;
	float f, r;
	
	for (a = 0; a < 10; a++)
		for (b = 0; b < 10; b++)
			if (a != b)
				for (x = 0; x < 10; x++)
					for (y = 0; y < 10; y++)
					{
						if (x != y)
						{
							ab = a*10 + b;
							xy = x*10 + y;
							f = (float)(ab)/(float)(xy);
							
									if (a == x && b!=0 && y!=0) { r = (float)(b)/(float)(y); if (r < 1.0 && r==f && a != 0) printf("%i%i/%i%i = %.2f -> %i/%i -> r = %f\n", a,b,x,y, f, b,y, r); prod *= ab; }
							else	if (a == y && b!=0 && x!=0) { r = (float)(b)/(float)(x); if (r < 1.0 && r==f && a != 0) printf("%i%i/%i%i = %.2f -> %i/%i -> r = %f\n", a,b,x,y, f, b,x, r); prod *= ab; }
							else	if (b == x && a!=0 && y!=0) { r = (float)(a)/(float)(y); if (r < 1.0 && r==f && b != 0) printf("%i%i/%i%i = %.2f -> %i/%i -> r = %f\n", a,b,x,y, f, a,y, r); prod *= ab; }
							else	if (b == y && a!=0 && x!=0) { r = (float)(a)/(float)(x); if (r < 1.0 && r==f && b != 0) printf("%i%i/%i%i = %.2f -> %i/%i -> r = %f\n", a,b,x,y, f, a,x, r); prod *= ab; }
						}
					}
	/*
		then do 
		16*19*26*49 = 387296
		64*95*65*98 = 38729600
		387296/38729600 = 0.01
		so result = 1/100 -> 100
	*/
	return 0;
}
							
