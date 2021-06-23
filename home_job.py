class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        sum_hw = 0
        count = 0
        for grades in self.grades.values():
            sum_hw += sum(grades)
            count += len(grades)
        return round(sum_hw / count, 2)

    def __str__(self):
        res = f'Имя: (self.name) \n' \
              f'Фамилия: (self.surname)\n' \
              f'Средняя оценка ДЗ: {self.get_avg_grade()}\n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super.__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f'Имя: (self.name) \n' \
              f'Фамилия: (self.surname)\n' \
              f'Средняя оценка ДЗ: {sum(self.grades) / len(self.grades) : .2f}\n'
        return res

    def __it__(self, other, student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            compare = self.get_avg_grade() < other_student.get_average_grade()
            if compare:
                print(f'f{self.name} {self.surname} учится хуже чем {other_student.name} {other_student.surname}')
            else:
                print(f'f{other_student.name} {other_student.surname} учится хуже чем {self.name} {self.surname}')
        return compare





class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: (self.name) \n' \
              f'Фамилия: (self.surname)\n'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

next_student = Student('Mike', 'Roman', 'your_gender')
next_student.courses_in_progress += ['Python']
next_student.finished_courses += ['Git']

cool_reviewer = Reviewer('Some', 'Fax')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 4)

