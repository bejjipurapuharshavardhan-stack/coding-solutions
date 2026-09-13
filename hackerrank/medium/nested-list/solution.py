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
    
