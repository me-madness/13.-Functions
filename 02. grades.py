grade = float(input())
def exam_solve(grade_score):
    if 2.00 <= grade_score <= 2.99:
         return "Fail"
    elif 3.00 <= grade_score <= 3.49: 
        return "Poor"
    elif 3.50 <= grade_score <= 4.49:
        return "Good"
    elif 4.50 <= grade_score <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_score <= 6.00:
        return "Excellent"
    else:
        return "No score"
    
print(exam_solve(grade))    