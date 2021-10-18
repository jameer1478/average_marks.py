def find_average_marks(marks):
    total_marks = len(marks)
    sum_marks = sum(marks)
    average_marks = sum_marks / total_marks
    return average_marks
    
def compute_grade(average_marks):
        if average_marks >= 80:
            grade = "A"
        elif average_marks >= 60:
            grade = "B"
        elif average_marks >= 50:
            grade = "C"
        else:
            grade = "F"
        return grade
    
marks = [55,64,73,59,83,92]
average_marks = find_average_marks(marks)
print("your average marks is:",average_marks)
grade = compute_grade(average_marks)
print("your grade is:",grade)