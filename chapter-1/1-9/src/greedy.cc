
extern bool Overlap( int, int, int, int );

int greedySolution( int N ) {
    int* isForbidden = new int[ N ];
    int  nMaxColors  = 0, i, k, j;
    for ( i = 0; i < N; ++i ) {
        for ( k = 0; k < nMaxColors; ++k ) {
            isForbidden[ k ] = false;
        }

        for ( j = 0; j < i; ++j ) {
            if ( Overlap( b[ j ], e[ j ], b[ i ], e[ i ] ) ) {
                isForbidden[ color[ j ] ] = true;
            }
        }
        for ( k = 0; k < nMaxColors; ++k ) {
            if ( !isForbidden[ k ] ) {
                break;
            }
        }

        if ( k < nMaxColors ) {
            color[ i ] = k;
        }
        else {
            color[ i ] = nMaxColors++;
        }
    }

    delete[] isForbidden;
    return nMaxColors;
}