class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [
    Student('Kim', 80),
    Student('Lee', 55),
    Student('Park', 90),
]

for s in students:
    sum += (int)(s.score)
print(sum)

for s in students:
    if s.score >= 80:
        print(s.name)