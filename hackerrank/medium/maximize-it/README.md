# Maximize It!

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a function $f(X) = X^{2}$. You are also given $K$ lists. The $i^{th}$ list consists of $N_i$ elements.

You have to pick one element from each list so that the value from the equation below is *maximized*: <br>

$S = (f(X_1) \; + f(X_2) \;+\;... \;+\; f(X_k))$%$M$

$X_i$ denotes the element picked from the $i^{th}$ list . Find the maximized value $S_{max}$  obtained. 

$\%$ denotes the modulo operator. 

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem. 




**Input Format**

The first line contains $2$ space separated integers $K$ and $M$.  
The next $K$ lines each contains an integer $N_i$, denoting the number of elements in the $i^{th}$ list, followed by $N_i$ space separated integers denoting the elements in the list. 

**Constraints**

$1 \le K \le 7$  
$1 \le M \le 1000$  
$1 \le N_i \le 7$  
$1 \le Magnitude \; of \; elements\;in\;list\; \le 10^{9}$  

**Output Format**

Output a single integer denoting the value $S_{max}$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T18:23:51.670Z  

```py
from itertools import product

def maximize_equation():
    K, M = map(int, input().split())
    
    lists = []
    for _ in range(K):
        elements = [int(x)**2 % M for x in input().split()[1:]]
        lists.append(elements)
        
    max_value = max(sum(combo) % M for combo in product(*lists))
    
    print(max_value)

if __name__ == '__main__':
    maximize_equation()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/maximize-it/problem)