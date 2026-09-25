# Check Strict Superset

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a set $A$ and $n$ other sets.   
Your job is to find whether set $A$ is a strict superset of each of the $N$ sets.   

Print `True`, if $A$ is a *strict superset* of each of the $N$ sets. Otherwise, print `False`. 

A strict superset has at least one element that does not exist in its subset.  

**Example**  
Set$([1, 3, 4])$ is a _strict superset_ of set$([1,3])$.  
Set$([1, 3, 4])$ is not a _strict superset_ of set$([1, 3, 4])$.   
Set$([1, 3, 4])$ is not a _strict superset_ of set$([1, 3, 5])$.  

**Input Format**

The first line contains the space separated elements of set $A$.  
The second line contains integer $n$, the number of other sets.   
The next $n$ lines contains the space separated elements of the other sets.  



**Constraints**

+ $0 < len(set(A)) < 501$   
+ $0 < N < 21 $  
+ $0 < len(otherSets) < 101$  



**Output Format**

Print `True` if set $A$ is a _strict superset_ of all other $N$ sets. Otherwise, print `False`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T05:51:19.388Z  

```py
set_A = set(map(int, input().split()))
n = int(input())

is_strict_superset = True

for _ in range(n):
    current_set = set(map(int, input().split()))
    
    if not (set_A.issuperset(current_set) and set_A != current_set):
        is_strict_superset = False
        break

print(is_strict_superset)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-check-strict-superset/problem)