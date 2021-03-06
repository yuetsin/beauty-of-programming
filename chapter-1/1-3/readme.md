# 1.3 一摞烙饼的排序

## ★★★

星期五的晚上，一帮同事在希格玛大厦附近的「硬盘酒吧」多喝了几杯。程序员喝了几杯之後谈什么呢？自然是算法问题。

有个同事说：「我以前在餐馆打工，顾客进场点非常多的烙饼。店里的饼大小不一，我习惯在到达顾客饭桌前，把一摞饼按照大小次序摆好——小的在上面，大的在下面。由于我一只手托着盘子，只好用另一只手，一次抓住最上面的几块饼，把他们上下颠倒个个儿，反复几次之後，这摞烙饼就排好序了。」

「我後来想，这实际上是个有趣的排序问题：假设有 $n$ 块大小不一的烙饼，那最少要翻几次，才能达到最後大小有序的结果呢？」

你能否写出一个程序，对于 $n$ 块大小不一的烙饼，输出最优化的翻饼过程呢？

## 解

这题跟普通的排序题都不一样…因为我们可以做的操作只有，`reverse(list[i:])` 这一件事；即，把从某一区间到尾部的这部分翻转。不能把饼子抽出来、不能交换任意两块饼。

不用烙饼来表述，这个问题的学名叫做 Sorting by Prefix Reversal。

在这种情况下，我们的排序该怎么进行呢？

不妨先设我们的饼子列表 `Cake` 是 shuffle 过的 `list(range(N)`。这样，当值为 `i` 的饼子到达 `i` 索引位置的时候，就可以认定为排序好了。

### Recursive Solution

#### Intuition

首先，可以观察到这道题是可以自底向上的。因为我们的「翻饼子」操作一定是涉及到 `list[i:]`，即饼摞的靠上一部分的；

所以，如果面积大于一定值的  `j`  个饼子都排好序了（已经好好地分布到 `Cake[:j]` 里了），那么就无需再管他们了，可以认为问题简化到了饼数量为 `N - j` 的地步。

最后，问题一定会简化到轻易的 `N = 2`，也就是只需要 0 次或 1 次翻转就能使他们有序。

这个 Recursive 是成立的。

#### Put cake `i` in place

因为上面的递归最终可以解，那么我们要做的就是通过一般的操作，把 `Cake(N)` 问题简化到 `Cake(N - 1)` 问题。也就是，把当前最大的那张饼（记为 `M`）放置到位。

分情况讨论：

* 假如 `M` 当前位于饼摞的底部（数组的头部），那么无需进行排序，直接推到 `N - 1`；

* 假如 `M` 当前位于饼摞的顶部（数组的尾部），那么只需要翻转整个饼摞，`M` 就被埋到了饼摞的底部，推到了 `N - 1`。

* 假如当前 `M` 位于索引 `k` 位置，其中 `k` 不是 0，也不是 `N - 1`。

我们的目的是把 `C[k]` 放到 `C[0]` 位置，而不考虑其他所有数字。在每个循环里都只保证最大的那块饼到位。

很容易就能想出办法：

1. 翻转 `Cake[k:]`，这样 `Cake[k]` 就到了数组尾部，也就是「饼摞」的顶部。

2. 翻转整个 `Cake`，这样第一步中在顶部的 `Cake[k]` 就被埋到了底部。

以上的讨论就覆盖了全部的情况。可以看到，由大到小地，每一次置位一张饼，需要的翻转次数可能是 0 次、1 次、或 2 次。

因此可以知道，对于 `N` 张饼组成的饼摞，我们需要的最多翻转数不会超过 `2 * (N - 1)`（因为最後两张饼不需要走讨论流程。）。

#### Optimization

上面的讨论只是证明了「通过翻转来排序饼」是可以实现的，而且给出了一个（非常粗的）上界。

实际的方案当然可以从各种方向上优化：比如，如果烙饼摞中的一些部分是已经排好序的，那么我们应该倾向于不去破坏那些有序性，而是优先把较小一些的烙饼摞给摞好，然后再把他们整体翻过来。

但是，这些都只是停留在「直觉」上的感觉。实际上计算机能解决的事情，还是只能靠穷举。

#### Exhaustion

给出 `N` 个饼组成的饼摞。

首先，我们没必要去翻动那些已经到位的、位于底部的大饼。所以我们要翻动的只是靠上的、较小的、顺序还没好的饼，记其数量为 `k`。

那么，我们一共有 `k - 1` 种翻动饼的选择；这可以作为一个 DFS。

假如我们所有的饼子都已经排序好了，或者当前的翻动次数已经超过了上界 $2 \times (N - 1)$，那么可以直接退出，不再继续往深层次递归了。

#### Code

参见 `./src/sample_exhaustion.cc` 和 `./src/sorting.hpp`。

### Optimized Solution

#### Upper Bound

我们上面的解法依赖于粗糙估计的上界 $(n - 1) \times 2$，也就是程序代码中的 `m_nMinSwap`。

穷竭法中，程序所进行的大部分尝试的结果都是超过上界并被丢弃，只有少部分很幸运的尝试可以最终得到有序的结果。

因此，如果我们能尽可能地缩小 `m_nMinSwap`，也就是上界的话，我们就可以大幅度地降低时间复杂度，减少很多不必要的递归。

#### Lower Bound

但是别忘了，我们还知道翻转烙饼次数的下界；

即，对于每一个当前的烙饼状态，至少需要翻转 $k$ 次才能实现有序（但并不保证一定存在恰好翻转 $k$ 次就能使得饼摞有序的办法）。

这个下界是可以用 $O(N)$ 时间找到的：

```python
def lowerbound(cakes: List[int]) -> int:
	count = 0

    for i in range(1, len(cakes)):
        if abs(cakes[i] - cakes[i - 1]) != 1:
            count += 1

    return count
```

也就是，如果在当前饼摞里存在 $k$ 个不连续的相邻饼对，那么就不可能通过小于 $k$ 次翻转来使他们有序。

知道了下界又能怎么样呢？注意源代码中这一部分剪枝：

```python
nEstimate = lowerbound(cakes)

if step + nEstimate > minSwap:
    return
```

注意 `step` 是我们已经翻转烙饼的次数。而 `nEstimate` 是为了使当前烙饼堆有序，所需要付出的最小翻转次数。两数加起来，就是当前情况下，我们所能找到的最优解的翻转次数的下界。

假如这个下界已经超过了 `minSwap`，那么我们应该立即放弃当前情况，它是不可能产生比 `minSwap` 步更优的解法的。

自然，我们是希望 `lowerbound` 产生的下界尽可能大，这样我们就能尽可能除去更多的枝。

#### Summary

根据我们上面的分析，为了进一步优化算法，我们能做的事情是尽可能使得上界和下界接近真实的最优解步数，这样能减少递归的次数，提高算法效率。

比较一下，在我们通过 `lowerbound` 进行算法优化的情况下，对下面这摞烙饼

```python
[3, 2, 1, 6, 5, 4, 9, 8, 7, 0]
```

所需要调用 `Search` 的次数是 $172126$ 次；但如果我们不对下界逾越的情况进行修剪，那么调用的次数将会增至 $575225200$ 次。

#### Extras

对于任意 $n$ 个烙饼组成的序列，所需要的翻转次数是有界的。

最大的下界结果是 $\frac {15n} {14}$，而最小的上界结果是 $\frac {5n + 5} {3}$。

而对于任意 $n$ 个烙饼堆，为了使他们有序而翻转的次数的最小值被称为第 $n$ 个烙饼数。

| $N$   | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   | 13   | 14   |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| $P_n$ | 0    | 1    | 3    | 4    | 5    | 7    | 8    | 9    | 10   | 11   | 13   | 14   | 15   | ?    |



## Applied Scene

看起来这题没有什么应用场景——对一般的数组而言，翻转 `k` 个数字所需要耗费的时间一般都很高。

然而，对于无向图而言，我们可以用 $O(1)$ 的时间复杂度来实现上述的「翻饼」操作——只需要断开并重建两条边即可。

或许这算是一个应用场景吧？
