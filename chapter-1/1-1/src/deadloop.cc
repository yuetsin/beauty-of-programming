int main() {
    int i = 0;

    while ( 1 ) {
        // will never stops since i overflows
        ++i;
    }

    // never will.
    return -1;
}