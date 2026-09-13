# Nested Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the names and grades for each student in a class of $N$ students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

**Note:** If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

**Example**  
$records = [[\text{"chi"}, 20.0], [\text{"beta"}, 50.0], [\text{"alpha"}, 50.0]]$

The ordered list of scores is $[20.0, 50.0]$, so the second lowest score is $50.0$.  There are two students with that score: $[\text{"beta", "alpha"}]$.  Ordered alphabetically, the names are printed as:
<pre>
alpha
beta
</pre>

**Input Format**

The first line contains an integer, $N$, the number of students. 	
The $2N$ subsequent lines describe each student over $2$ lines.  
- The first line contains a student's name.  
- The second line contains their grade. 


**Constraints**

- $2 \le N \le 5$  
- There will always be one or more students having the second lowest grade. 

**Output Format**

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T06:00:18.452Z  

```py
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    all_scores = []
    for item in records:
        student_score = item[1]
        all_scores.append(student_score)
    
    unique_scores = list(set(all_scores))
    unique_scores.sort()
    second_lowest = unique_scores[1]
    
    names_print = []
    for item in records:
        student_name = item[0]
        student_score = item[1]
        
        if student_score == second_lowest:
            names_print.append(student_name)
    names_print.sort()
    for name in names_print:
        print(name)
    

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/nested-list/problem)