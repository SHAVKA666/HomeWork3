class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() > other.average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() < other.average_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() > other.average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

student1 = Student('Иван', 'Иванов', 'М')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Мария', 'Петрова', 'Ж')
student2.courses_in_progress = ['Python', 'Java']
student2.finished_courses = ['Английский для IT']

mentor1 = Mentor('Надежда', 'Орлова')
mentor1.courses_attached = ['Python', 'Java']

mentor2 = Mentor('Павел', 'Кищик')
mentor2.courses_attached = ['Git', 'Java']

lecturer1 = Lecturer('Петр', 'Сидоров')
lecturer1.courses_attached = ['Python', 'Java']

lecturer2 = Lecturer('Анна', 'Смирнова')
lecturer2.courses_attached = ['Python', 'Git']

reviewer1 = Reviewer('Ольга', 'Козлова')
reviewer1.courses_attached = ['Python', 'Git']

reviewer2 = Reviewer('Дмитрий', 'Морозов')
reviewer2.courses_attached = ['Java', 'Python']

def average_grade_students(list_of_students, course):
    list_all_grades = []
    for student in list_of_students:
        if course in student.grades:
            list_all_grades.extend(student.grades[course])
    if len(list_all_grades) == 0:
        return 0 
    
    return sum(list_all_grades) / len(list_all_grades)

def average_grade_lecturers(list_of_lecturers, course):
    list_all_grades = []
    for lecturer in list_of_lecturers:
        if course in lecturer.grades:
            list_all_grades.extend(lecturer.grades[course])
    if len(list_all_grades) == 0:
        return 0 
    
    return sum(list_all_grades) / len(list_all_grades)


