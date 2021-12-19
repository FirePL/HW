student_scores = {
'Ivan': 5.00,
'Alexander': 3.50,
'Maria': 5.50,
'Georgi': 5.00
}
min_students_scores = { students: scores for students, scores in list(student_scores.items()) if scores == min(student_scores.values())}
max_students_scores = { students: scores for students, scores in list(student_scores.items()) if scores == max(student_scores.values())}

for student, scores in min_students_scores.items():
    print("{} - {}".format(student, scores))

for student, scores in max_students_scores.items():
    print("{} - {}".format(student, scores))    