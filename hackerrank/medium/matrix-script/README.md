# Matrix Script

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Neo has a complex *matrix script*. The *matrix script* is a $N $ X $ M$ grid of strings. It consists of alphanumeric characters, spaces and  symbols (!,@,#,$,%,&).

<img src="https://s3.amazonaws.com/hr-challenge-images/12524/1442753362-1075bd12d9-Capture.JPG" title="Capture.JPG" />

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a *single* space '$ \ $' for better readability.  

Neo feels that there is no need to use '`if`' conditions for decoding.

*Alphanumeric characters* consist of: [A-Z, a-z, and 0-9].

**Input Format**

The first line contains space-separated integers $N$ (rows) and $M$ (columns) respectively.  
The next $N$ lines contain the row elements of the *matrix script*. 

__Constraints__  

$0 < N, M < 100$  

**Note**: A $0$ score will be awarded for using '`if`' conditions in your code.

**Output Format**

Print the decoded *matrix script*.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T16:38:31.924Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
decoded_string = "".join([matrix[i][j] for j in range(m) for i in range(n)])

final_string = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decoded_string)

print(final_string)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/matrix-script/problem)