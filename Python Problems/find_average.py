# goal to find the average score for a given student 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    
    avg_scores = student_marks[query_name]
    average = sum(avg_scores)/len(avg_scores)
    print("%.2f" %average)                          # print out two decimal places