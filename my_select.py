from sqlalchemy import select, func
from connect_db import db_session
from models import StudentsGroup, Student, Teacher, Subject, Mark


def select_1(db_session=None):
    query = db_session.execute(
        select(Student.name, func.avg(Mark.mark).label('avg_mark'))
        .join(Mark, Student.id == Mark.student_id)
        .group_by(Student.name)
        .order_by(func.avg(Mark.mark).desc())
        .limit(5)
    ).all()

    return query


def select_2(db_session=None):
    query = db_session.execute(
        select(Student.name, func.avg(Mark.mark).label('avg_mark'))
        .join(Mark, Student.id == Mark.student_id)
        .join(Subject, Subject.id == Mark.subject_id)
        .where(Subject.name == 'Філолог')
        .group_by(Student.name)
        .order_by(func.avg(Mark.mark).desc())
        .limit(1)
    ).all()

    return query


def select_3(db_session=None):
    query = db_session.execute(
        select(StudentsGroup.name, func.avg(Mark.mark).label('avg_mark'))
        .join(Student, StudentsGroup.id == Student.group_id)
        .join(Mark, Student.id == Mark.student_id)
        .join(Subject, Subject.id == Mark.subject_id)
        .where(Subject.name == 'Філолог')
        .group_by(StudentsGroup.name)
        .order_by(func.avg(Mark.mark).desc())
    ).all()

    return query


def select_4(db_session=None):
    query = db_session.execute(
        select(func.avg(Mark.mark).label('avg_mark'))
    ).all()

    return query


def select_5(db_session=None):
    query = db_session.execute(
        select(Subject.name)
        .where(Subject.teacher_id == 4)
    ).all()

    return query


def select_6(db_session=None):
    query = db_session.execute(
        select(Student.name)
        .where(Student.group_id == 1)
    ).all()

    return query


def select_7(db_session=None):
    query = db_session.execute(
        select(Student.name.label('student_name'), Mark.mark)
        .join(Mark, Student.id == Mark.student_id)
        .join(Subject, Subject.id == Mark.subject_id)
        .join(StudentsGroup, Student.group_id == StudentsGroup.id)
        .where(
            StudentsGroup.id == 2,
            Subject.id == 3
        )
    ).all()

    return query


def select_8(db_session=None):
    query = db_session.execute(
        select(Teacher.name, func.avg(Mark.mark).label('avg_mark'))
        .join(Subject, Subject.teacher_id == Teacher.id)
        .join(Mark, Mark.subject_id == Subject.id)
        .group_by(Teacher.id, Teacher.name)
        .order_by(func.avg(Mark.mark).desc())
    ).all()

    return query


def select_9(db_session=None):
    query = db_session.execute(
        select(Subject.name.label('course_name'))
        .join(Mark, Subject.id == Mark.subject_id)
        .join(Student, Student.id == Mark.student_id)
        .where(Student.id == 4)
        .distinct()
    ).all()

    return query


def select_10(db_session=None):
    query = db_session.execute(
        select(Subject.name.label('course_name'))
        .join(Mark, Subject.id == Mark.subject_id)
        .join(Student, Student.id == Mark.student_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .where(
            Teacher.id == 3,
            Student.id == 5
        )
        .distinct()
    ).all()

    return query


if __name__ == '__main__':
    select_1(db_session)
    select_2(db_session)
    select_3(db_session)
    select_4(db_session)
    select_5(db_session)
    select_6(db_session)
    select_7(db_session)
    select_8(db_session)
    select_9(db_session)
    select_10(db_session)
