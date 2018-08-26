# 字符串匹配

- 文本串长度：n
- 模式串长度：m

## 1、朴素算法
时间复杂度：O(mn)  
空间复杂度：O(1)  
代码：[Naive_Matching.py](Code/Naive_Matching.py)

## 2、KMP算法
时间复杂度：O(m+n)  
空间复杂度：O(m)  
代码：[KMP_Matching.py](Code/KMP_Matching.py)

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

`p[k] == p[j]` → `next[j+1] = next[j] + 1 = k + 1`  
`p[k] != p[j]` → `p[h] == p[j]` ：`next[j+1] = next[k] + 1 = next[next[j]] + 1 = h + 1`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`p[h] != p[j]` ：重复  
