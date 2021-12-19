student_scores = {
'Ivan': 5.00,
'Alexander': 3.50,
'Maria': 5.50,
'Georgi': 5.00
}
#del student_scores[student_scores.keys if student_scores.values() < 4]
del student_scores['Alexander']
best_students_scores = student_scores

for student, scores in best_students_scores.items():
    print("{} - {}".format(student, scores))