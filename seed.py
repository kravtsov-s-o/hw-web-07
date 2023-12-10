from connect_db import db_session
from models import StudentsGroup, Student, Teacher, Subject, Mark
from datetime import datetime
from faker import Faker
from random import randint

NUMBER_OF_STUDENTS = 50
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 8
NUMBER_OF_TEACHERS = 5
MAX_NUMBER_OF_MARKS = 20


def generate_and_prepare_data(
        count_groups: int = NUMBER_OF_GROUPS,
        count_students: int = NUMBER_OF_STUDENTS,
        count_teachers: int = NUMBER_OF_TEACHERS,
        count_subjects: int = NUMBER_OF_SUBJECTS):
    fake_data = Faker('uk_UA')

    groups = [StudentsGroup(name=f'Група {group_id}') for group_id in range(1, count_groups + 1)]
    students = [Student(name=fake_data.name(), group_id=randint(1, len(groups))) for _ in range(count_students)]
    teachers = [Teacher(name=fake_data.name()) for _ in range(count_teachers + 1)]
    subjects = [Subject(name=fake_data.job(), teacher_id=randint(1, len(teachers))) for _ in range(count_subjects)]

    marks = []
    for i, student_name in enumerate(students):
        for j, subject_name in enumerate(subjects):
            for _ in range(randint(10, MAX_NUMBER_OF_MARKS)):
                date = datetime(2022, randint(1, 12), randint(1, 28)).date()
                mark_value = randint(1, 10)
                mark = Mark(student_id=i + 1, subject_id=j + 1, mark=mark_value, date=date)
                marks.append(mark)

    return groups, students, teachers, subjects, marks


if __name__ == '__main__':
    groups, students, teachers, subjects, marks = generate_and_prepare_data()

    db_session.query(StudentsGroup).delete()
    db_session.query(Student).delete()
    db_session.query(Teacher).delete()
    db_session.query(Subject).delete()
    db_session.query(Mark).delete()

    db_session.add_all(groups)
    db_session.commit()

    db_session.add_all(students)
    db_session.commit()

    db_session.add_all(teachers)
    db_session.commit()

    db_session.add_all(subjects)
    db_session.commit()

    db_session.add_all(marks)
    db_session.commit()

    db_session.close()
