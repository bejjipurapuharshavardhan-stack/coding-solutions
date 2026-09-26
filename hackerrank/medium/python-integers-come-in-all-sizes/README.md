# Integers Come In All Sizes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: $2^{31}-1$ (c++ int) or $2^{63} - 1$ (C++ long long int).    

As we know, the result of $a^b$ grows really fast with increasing $b$.  

Let's do some calculations on very large integers.  

**Task**  
Read four numbers, $a$, $b$, $c$, and $d$, and print the result of $a^b + c^d$.  

**Input Format**  
Integers $a$, $b$, $c$, and $d$ are given on four separate lines, respectively.

**Constraints**  
$1 \le a \le 1000$  
$1 \le b \le 1000$  
$1 \le c \le 1000$  
$1 \le d \le 1000$  

**Output Format**  
Print the result of $a^b + c^d$ on one line.  

**Sample Input**  

    9
    29
    7
    27
    
**Sample Output**  

    4710194409608608369201743232  
    
**Note**: This result is bigger than $2^{63} - 1$. Hence, it won't fit in the long long int of C++ or a 64-bit integer.  

**Input Format**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-26T04:22:26.750Z  

```py
a, b, c, d = [int(input()) for _ in range(4)]

res = pow(a,b) + pow(c,d)
print(res)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem)