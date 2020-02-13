#include "timer.h"
#include <iostream>

using namespace std;

typedef unsigned char BYTE;

int main() {
    clock_t ts = 0;
    clock_t te = 0;

    ts = clock();

    BYTE i = 81;
    while ( i-- ) {
        if ( i / 9 % 3 == i % 9 % 3 )
            continue;
        printf( "A = %d, B = %d\n", i / 9 + 1, i % 9 + 1 );
    }
    te = clock();

    printf( "solution #1 time elapsed: %f s\n", seconds( ts, te ) );
    return 0;
}