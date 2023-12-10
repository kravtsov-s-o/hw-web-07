from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime, Date

Base = declarative_base()


# Table StudentsGroups
class StudentsGroup(Base):
    __tablename__ = 'students_groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())


# Table Students
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey(StudentsGroup.id, ondelete="SET NULL", onupdate="CASCADE"))
    created_at = Column(DateTime, default=datetime.now())


# Table Teachers
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


# Table Subjects
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete="SET NULL", onupdate="CASCADE"))
    created_at = Column(DateTime, default=datetime.now())
    teacher = relationship("Teacher", backref="subjects")


# Table Marks
class Mark(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE", onupdate="CASCADE"))
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete="CASCADE", onupdate="CASCADE"))
    subject = relationship("Subject", backref="marks")
    mark = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.now())



