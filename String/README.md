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
![KMP算法](https://github.com/Donrinho/Algorithm/raw/master/String/picture/02.jpg)

## KMP算法的关键：求next[j]
即查找`pattern[0:j]`的最大相等k前缀和k后缀（不包括自身）
