#define SETBIT(x,i)  (x | (x<<i))

#define CLRBIT(x,i)  (x & ~(x<<i))
#define ISSET(x,i)  ((x & (x<<i)) !=0)
#define FLIPBIT(x,i)  (x ^ (x<<i))

