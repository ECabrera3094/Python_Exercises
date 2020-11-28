def gradingStudents(grades):
    # Write your code here
    list_FinalGrades = []
    
    list_Grades = grades.copy()
    
    print(list_Grades)

    for i in range(len(grades)):
        while grades[i] % 5 != 0:
            grades[i] += 1

        list_FinalGrades.append(grades[i])

        if list_Grades[i] < 38:
            list_FinalGrades[i] = list_Grades[i]
        elif list_FinalGrades[i] - list_Grades[i] < 3:
            pass
        elif list_FinalGrades[i] - list_Grades[i] == 3:
            list_FinalGrades[i] = list_Grades[i]
        elif list_FinalGrades[i] - list_Grades[i] > 3:
            list_FinalGrades[i] = list_Grades[i]
        
    return list_FinalGrades

if __name__ == '__main__':
    print(gradingStudents([73,67,38,33]))
    print(gradingStudents([23,80,96,18,73,78,60,60,15,45,15,10,5,46,87,33,60,14,71,65,2,5,97,0]))