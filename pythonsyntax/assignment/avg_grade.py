import random as r
import os
grades=[n*0.5 for n in range(2,10)]
sub = {}
def generate_grade():
  for i in range(5):
   student_num="student"+str(i+1)
   sub[student_num]={}
   for j in range(5):
    r_grade=r.choice(grades)
    sub_name=f"subject {j+1}"
    subject_credit = r.randint(1, 3)
    sub_grade=r.choice(grades)

    sub[student_num][sub_name]={"credit":subject_credit,"grade":sub_grade}
def avg_grade():
    generate_grade()
    for student, subjects in sub.items():
        total_score = 0
        total_credit = 0
        for subject, info in subjects.items():
            credit = info['credit']
            grade = info['grade']
            total_score += credit * grade
            total_credit += credit
        avg = total_score / total_credit if total_credit != 0 else 0
        print(f"{student}의 평균 평점: {avg:.2f}")