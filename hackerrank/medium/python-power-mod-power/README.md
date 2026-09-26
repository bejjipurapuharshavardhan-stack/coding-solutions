# Power - Mod Power

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

So far, we have only heard of Python's powers. Now, we will witness them!  

Powers or exponents in Python can be calculated using the built-in power function. Call the power function $a^b$ as shown below:  

	>>> pow(a,b) 
    
or 

	>>> a**b

It's also possible to calculate $a^b \mod m$.  

	>>> pow(a,b,m)  
    
This is very helpful in computations where you have to print the resultant % mod.  

**Note**: Here, $a$ and $b$ can be floats or negatives, but, if a third argument is present, $b$ cannot be negative.  

**Note**: Python has a math module that has its own *pow()*. It takes two arguments and returns a float. It is uncommon to use *math.pow()*.  

**Task**  
You are given three integers: $a$, $b$, and $m$. Print two lines.  
On the first line, print the result of *pow(a,b)*. On the second line, print the result of *pow(a,b,m)*.  

**Input Format**  
The first line contains $a$, the second line contains $b$, and the third line contains $m$.  

**Constraints**  
$1 \le a \le 10$   
$1 \le b \le 10$  
$2 \le m \le 1000$  

**Sample Input**  

    3
    4
    5
    
**Sample Output**  

    81
    1


**Input Format**

 

**Constraints**

 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-26T04:12:17.143Z  

```py
a = int(input())
b  = int(input())
m = int(input())

res1 = pow(a,b)
res2 = pow(a,b,m)
print(res1)
print(res2)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-power-mod-power/problem)