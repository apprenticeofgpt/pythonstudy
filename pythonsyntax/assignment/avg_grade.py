import random as r

class grade:
    def __init__(self, student_count=5, subject_count=5):  # 학생 수 5명 과목 수 5개
        self.student_count = student_count
        self.subject_count = subject_count
        self.grades = [n * 0.5 for n in range(2, 10)]  # 학점
        self.sub = {}

    def generate_grades(self):
        self.sub = {}
        for i in range(self.student_count):
            student_num = f"student{i+1}"
            self.sub[student_num] = {}
            for j in range(self.subject_count):
                subject_name = f"subject {j+1}"
                subject_credit = r.randint(1, 3)
                subject_grade = r.choice(self.grades)
                self.sub[student_num][subject_name] = {
                    "credit": subject_credit,
                    "grade": subject_grade,
                }

    def avg_grade(self):
        for student, subjects in self.sub.items():
            total_score = 0
            total_credit = 0
            for subject, info in subjects.items():
                credit = info["credit"]
                grade = info["grade"]
                total_score += credit * grade
                total_credit += credit
            avg = total_score / total_credit if total_credit != 0 else 0
            print(f"{student}'s avg: {avg:.2f}")

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for student, subjects in self.sub.items():
                f.write(f"{student}'s grade\n")
                f.write("-" * 20 + "\n")
                for subject, info in subjects.items():
                    grade = info["grade"]
                    credit = info["credit"]
                    f.write(f"{subject} - grade: {grade}, credit: {credit}\n")
                f.write("\n")
        print(f"saved as {filename}.")

    def save_to_file_with_avg(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for student, subjects in self.sub.items():
                total_score = 0
                total_credit = 0
                f.write(f"{student}'s grade\n")
                f.write("-" * 20 + "\n")
                for subject, info in subjects.items():
                    grade = info["grade"]
                    credit = info["credit"]
                    total_score += credit * grade
                    total_credit += credit
                    f.write(f"{subject} - grade: {grade}, credit: {credit}\n")
                avg = total_score / total_credit if total_credit != 0 else 0
                f.write(f"grade (GPA): {avg:.2f}\n\n")
        print(f"saved as{filename}.")
