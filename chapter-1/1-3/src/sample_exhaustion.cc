#include "sorting.hpp"

int main() {

    int cakes[]    = { 1, 4, 2, 6, 3, 5, 7, 8, 10, 9 };
    int cake_count = sizeof( cakes ) / sizeof( cakes[ 0 ] );

    CPrefixSorting cps = CPrefixSorting();

    cps.Run( cakes, cake_count );
    cps.Output();

    return EXIT_SUCCESS;
}