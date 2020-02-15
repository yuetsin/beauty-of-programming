#include <cassert>
#include <cstdio>

class CPrefixSorting {
public:
    CPrefixSorting() {
        m_nCakeCnt = 0;
        m_nMaxSwap = 0;
    }

    //
    // 计算烙饼的翻转信息。
    // @param
    // pCakeArray   存储烙饼索引的数组
    // nCakeCnt     烙饼的个数
    //
    void Run( int* pCakeArray, int nCakeCnt ) {
        Init( pCakeArray, nCakeCnt );

        m_nSearch = 0;

        Search( 0 );
    }

    //
    // 输出烙饼具体翻转的次数
    //
    void Output() {
        for ( int i = 0; i < m_nMaxSwap; ++i ) {
            printf( "%d ", m_SwapArray[ i ] );
        }
        printf( "\nSearch Times: %d\n", m_nSearch );
        printf( "Total Swap Times: %d\n", m_nMaxSwap );
    }

private:
    //
    // 初始化数组信息
    // @param
    // pCakeArray   存储烙饼索引的数组
    // nCakeCnt     烙饼的个数
    //
    void Init( int* pCakeArray, int nCakeCnt ) {

        assert( pCakeArray );
        assert( nCakeCnt > 0 );

        m_nCakeCnt = nCakeCnt;

        // 初始化烙饼数组
        m_CakeArray = new int[ m_nCakeCnt ];
        assert( m_CakeArray );

        for ( int i = 0; i < m_nCakeCnt; ++i ) {
            m_CakeArray[ i ] = pCakeArray[ i ];
        }

        // 设置最多的翻转次数
        m_nMaxSwap = UpBound( m_nCakeCnt );

        // 初始化交换结果数组
        m_SwapArray = new int[ m_nMaxSwap ];
        assert( m_SwapArray );

        // 初始化中间交换信息
        m_ReverseCakeArray = new int[ m_nCakeCnt ];

        for ( int i = 0; i < m_nCakeCnt; ++i ) {
            m_ReverseCakeArray[ i ] = m_CakeArray[ i ];
        }

        m_ReverseCakeArraySwap = new int[ m_nMaxSwap ];
    }

    //
    // 寻找当前翻转的上界
    //
    int UpBound( int nCakeCnt ) {
        return nCakeCnt * 2;
    }

    //
    // 寻找当前翻转的下界
    //
    int LowerBound( int* pCakeArray, int nCakeCnt ) {
        int t, ret = 0;

        // 根据当前数组的有序情况判断最少需要交换的次数
        for ( int i = 1; i < nCakeCnt; ++i ) {
            t = pCakeArray[ i ] - pCakeArray[ i - 1 ];

            if ( !( ( t == 1 ) || ( t == -1 ) ) ) {
                ++ret;
            }
        }

        return ret;
    }

    //
    // 排序函数
    //
    void Search( int step ) {
        int nEstimate;
        ++m_nSearch;

        // 估算这次搜索需要的最小交换次数
        nEstimate = LowerBound( m_ReverseCakeArray, m_nCakeCnt );

        // 已经超过上界，就不要继续搜索了
        if ( step + nEstimate > m_nMaxSwap )
            return;

        // 如果已经排好序，就直接输出结果
        if ( IsSorted( m_ReverseCakeArray, m_nCakeCnt ) ) {
            if ( step < m_nMaxSwap ) {
                m_nMaxSwap = step;
                for ( int i = 0; i < m_nMaxSwap; ++i ) {
                    m_SwapArray[ i ] = m_ReverseCakeArraySwap[ i ];
                }
                return;
            }
        }

        // 如果尚未排好序，那么递归地继续
        for ( int i = 1; i < m_nCakeCnt; ++i ) {
            Revert( 0, i );
            m_ReverseCakeArraySwap[ step ] = i;
            Search( step + 1 );
            Revert( 0, i );
        }
    }

    //
    // 判断饼摞是否已经有序
    //
    bool IsSorted( int* pCakeArray, int nCakeCnt ) {
        for ( int i = 1; i < nCakeCnt; ++i ) {
            if ( pCakeArray[ i - 1 ] > pCakeArray[ i ] ) {
                return false;
            }
        }

        return true;
    }

    //
    // 翻转烙饼动作
    //
    void Revert( int nBegin, int nEnd ) {
        assert( nEnd > nBegin );

        int i, j, t;
        for ( i = nBegin, j = nEnd; i < j; ++i, --j ) {
            t                       = m_ReverseCakeArray[ i ];
            m_ReverseCakeArray[ i ] = m_ReverseCakeArray[ j ];
            m_ReverseCakeArray[ j ] = t;
        }
    }

private:
    int* m_CakeArray;             // 烙饼信息数组
    int  m_nCakeCnt;              // 烙饼的个数
    int  m_nMaxSwap;              // 最多的交换次数。初始状态下为 n * 2，随後会不断减小
    int* m_SwapArray;             // 交换结果数组
    int* m_ReverseCakeArray;      // 当前翻转烙饼信息数组
    int* m_ReverseCakeArraySwap;  // 当前翻转烙饼交换结果数组
    int  m_nSearch;               // 当前搜索次数
};