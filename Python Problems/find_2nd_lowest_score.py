# goal to find all students whose score is the second lowest score in the class

if __name__ == '__main__':
    students = []             # nested list 
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        student = [] 
        student.append(name)
        student.append(score)
        
        students.append(student)
        
    min = 500
    for student in students:
        if student[1] < min:
            min = student[1]
            
    students2 = [] 
    for student in students: 
        if student[1] > min:
            students2.append(student)
        
    # find the minimum first
    min2 = 500
    for student in students2:
        if student[1] < min2:
            min2 = student[1]
    
    # find all students whose score is the minimum score 
    low_names = [] 
    for student in students2:
        if student[1] == min2:
            low_names.append(student[0])
    
    low_names.sort()    # alphabetize names list
    for name in low_names:
        print(name)
        
        