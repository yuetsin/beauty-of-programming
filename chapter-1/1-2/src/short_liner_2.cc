#include "timer.h"
#include <iostream>

using namespace std;

struct {
    unsigned char a : 4;
    unsigned char b : 4;
} i;

int main() {
    clock_t ts = 0;
    clock_t te = 0;

    ts = clock();

    for ( i.a = 1; i.a <= 9; i.a++ )
        for ( i.b = 1; i.b <= 9; i.b++ )
            if ( i.a % 3 == i.b % 3 )
                printf( "A = %d, B = %d\n", i.a, i.b );
    te = clock();

    printf( "solution #2 time elapsed: %f s\n", seconds( ts, te ) );
    return 0;
}