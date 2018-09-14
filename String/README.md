# 字符串匹配

- 文本串长度：n
- 模式串长度：m

## 1、朴素算法
时间复杂度：O(mn)  
空间复杂度：O(1)  
代码：[Naive_Matching.py](code/Naive_Matching.py)

## 2、KMP算法
时间复杂度：O(m+n)  
空间复杂度：O(m)  
代码：[KMP_Matching.py](code/KMP_Matching.py)

## 两种算法的区别

| 算法  | 判断                    | 匹配成功 | 匹配失败        |
| :---: | :---:                   | :---:    | :---:           |
| Naive | `text[i+j] == pattern[j]` | `i++  j++` | `i++`   `j=0`       |
| KMP   | `text[i+j] == pattern[j]` | `i++  j++` | `i`不变 `j=next[j]` |

### 朴素算法

![朴素算法](https://github.com/Donrinho/Algorithm/raw/master/String/picture/01.jpg)

### KMP算法

![KMP算法](https://github.com/Donrinho/Algorithm/raw/master/String/picture/02.jpg)

## KMP算法的关键：求next[j]
即查找`pattern[0:j]`的最大相等k前缀和k后缀（不包括自身）
**例子：**  
假设模式串为：`'abcabde'`  
当`j=0`时，`''`，定义`k=-1`  
当`j=1`时，`'a'`，`k=0`  
当`j=2`时，`'ab'`，`k=0`  
当`j=3`时，`'abc'`，`k=0`  
当`j=4`时，`'abca'`，`k=1`  
当`j=5`时，`'abcab'`，`k=2`  
当`j=6`时，`'abcabd'`，`k=0`  

| 模式串  | `a` | `b` | `c` | `a` | `b` | `d` | `e` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `j` | `0` | `1` | `2` | `3` | `4` | `5` | `6` |
| `pnext[j]` | `-1` | `0` | `0` | `0` | `1` | `2` | `0` |

规律：`pnext[1]`一定等于`0`  

![pnext](https://github.com/Donrinho/Algorithm/raw/master/String/picture/03.jpg)

`p[k] == p[j]` **→** `next[j+1] = next[j] + 1 = k + 1`  
`p[k] != p[j]` **→** `p[h] == p[j]` ：`next[j+1] = next[k] + 1 = next[next[j]] + 1 = h + 1`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`p[h] != p[j]` ：重复  

求next[j]的函数如下：
```python
def gen_pnext(p):
    j, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while j < m - 1:
        if k == -1 or p[j] == p[k]:
            j, k = j + 1, k + 1
            pnext[j] = k
        else:
            k = pnext[k]
    return pnext
```
**注：**  
- `j`表示索引，`k`表示`next[j]`，`m`表示长度
- `while`循环从`pnext[1]`到`pnext[len(p)]`
- 由于`next[1]`一定等于`0`，那么`next[0]`一定等于`-1`，所以`k=-1`既表示开头，也为了递归式的统一

## KMP算法的改进
考虑文本串与模式串匹配失败时，模式串会从匹配失败处`j`滑动到`k`处
对应求next[j]的函数中第7行：`pnext[j] = k`
由于p[j]与文本串匹配失败，所以如果满足`p[j] == p[k]`，应继续滑动到`pnext[k]`处，提高效率
即：`pnext[j] == k` 并且 `p[j] == p[k]` ，`pnext[j]`可以直接等于`pnext[k]`

改进后求next[j]的函数如下：
```python
def gen_pnext(p):
    j, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while j < m - 1:
        if k == -1 or p[j] == p[k]:
            j, k = j + 1, k + 1
            if p[j] == p[k]:
                pnext[j] = pnext[k]
            else:
                pnext[j] = k
        else:
            k = pnext[k]
    return pnext
```

改进后代码：[KMP_Matching_new.py](code/KMP_Matching_new.py)

## KMP算法的应用
[Power Strings:](http://poj.org/problem?id=2406)&nbsp;POJ2406
若字符串S是由子串T循环n次得到，求最大的n
**例如：**
输入：
abcd
aaaa
ababab
输出：
1
4
3

原有的KMP算法中求得的`pnext`数组长度与模式串相同，但`pnext[0:n-1]`数组代表的是`p`的最大相等k前缀和k后缀（不包括自身），所以需要在末尾扩充一个元素使其包括自身，修改后的`pnext[0:n]`的最后一位代表整个字符串的最大相等k前缀和k后缀

求最大的循环次数的方法：
判断`len(p)`是否能被`len(p)-pnext[n]`整除

原理见下图：

![Power Strings](https://github.com/Donrinho/Algorithm/raw/master/String/picture/04.jpg)

完整代码：[Power_Strings.py](code/Power_Strings.py)