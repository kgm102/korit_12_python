class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grade = {}

    def add_grade(self, subject, score):
        self.grade[f'{subject}'] = score

    def get_average_grade(self):
        print(f'학생 이름: {self.name}')
        print(f'평균 성적: {sum(self.grade.values())/ (len(self.grade))}점')


st1 = Student('김일', 1)
st1.add_grade('국어',90)
st1.add_grade('수학',80)
st1.add_grade('사회',70)
st1.add_grade('과학',100)
st1.get_average_grade()

