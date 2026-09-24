# Check Subset

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two sets, $A$ and $B$.   
Your job is to find whether set $A$ is a subset of set $B$.<br>  
If set $A$ is subset of set $B$, print __True__.<br>
If set $A$ is not a subset of set $B$, print __False__.



**Input Format**

The first line will contain the number of test cases, $T$. <br>
The first line of each test case contains the number of elements in set $A$.<br>
The second line of each test case contains the space separated elements of set $A$.<br>
The third line of each test case contains the number of elements in set $B$.<br>
The fourth line of each test case contains the space separated elements of set $B$.<br>

**Constraints**

+ $0 < T < 21$ 
+ $0 < \text{Number of elements in each set} < 1001$

**Output Format**

Output __True__ or __False__ for each test case on separate lines.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-24T07:25:57.193Z  

```py
for _ in range(int(input())):
    a_len = int(input())
    set1 = set(map(int, input().split()))
    b_len = int(input())
    set2 = set(map(int, input().split()))
    print(set1.issubset(set2))
    

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-check-subset/problem)