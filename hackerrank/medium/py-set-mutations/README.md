# Set Mutations

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

We have seen the applications of *union, intersection, difference* and *symmetric difference* operations, but these operations do not make any changes or mutations to the set.  

**We can use the following operations to create mutations to a set:**

__.update()__ or __`|=`__ <br>
Update the set by adding elements from an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
```

__.intersection_update()__ or __`&=`__<br>
Update the set by keeping only the elements found in it and an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
```

__.difference_update()__ or __`-=`__<br>
Update the set by removing elements found in an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
```

__.symmetric_difference_update()__ or __`^=`__<br>
Update the set by only keeping the elements found in either set, but not in both.
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
```

---

__TASK__<br>
You are given a set $A$ and $N$ number of other sets. These $N$ number of sets have to perform some specific mutation operations on set $A$.

Your task is to execute those operations and print the sum of elements from set $A$.


**Input Format**

The first line contains the number of elements in set $A$.<br>
The second line contains the space separated list of elements in set $A$.<bR>
The third line contains integer $N$, the number of other sets.<br>
The next $2*N$ lines are divided into $N$ parts containing two lines each.<br>
The first line of each part contains the space separated entries of the _operation name_ and the _length of the other set_.<br>
The second line of each part contains space separated list of elements in the other set.<bR>

$0 <$ *len(set(__A__))* $< 1000$ <br>
$0 <$ *len(otherSets)* $< 100$ <br>
$0 < N < 100$

**Output Format**

Output the sum of elements in set $A$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T05:23:55.099Z  

```py
num_elements_A = int(input())
set_A = set(map(int, input().split()))
num_N = int(input())

for _ in range(num_N):
    command_line = input().split()
    command = command_line[0]
    
    other_set = set(map(int, input().split()))
    
    if command == "update":
        set_A.update(other_set)
    elif command == "intersection_update":
        set_A.intersection_update(other_set)
    elif command == "difference_update":
        set_A.difference_update(other_set)
    elif command == "symmetric_difference_update":
        set_A.symmetric_difference_update(other_set)
        
print(sum(set_A))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-set-mutations/problem)