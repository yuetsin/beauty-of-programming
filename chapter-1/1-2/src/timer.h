#include <time.h>

inline double seconds( const clock_t ts, const clock_t te ) {
    return ( double )( te - ts ) / CLOCKS_PER_SEC;
}
