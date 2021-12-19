student_scores = {
'Ivan': 5.00,
'Alexander': 3.50,
'Maria': 5.50,
'Georgi': 5.00
}
best_students_scores = { students: scores for students, scores in list(student_scores.items()) if scores > 4}

for student, scores in best_students_scores.items():
    print("{} - {}".format(student, scores))