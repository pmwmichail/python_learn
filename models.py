from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


DATABASE_NAME = 'univerdb'

Base = declarative_base()


staff_faculty = Table('staff_faculty', Base.metadata,
    Column('staff_id', Integer, ForeignKey('staff.id')),
    Column('faculty_id', Integer, ForeignKey('faculty.id'))
)

exam_student = Table('exam_student', Base.metadata,
    Column('exam_id', Integer, ForeignKey('exam.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
)


class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    exam = relationship('Exam')
    hr_record = relationship('HRRecord')


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    group_id = Column(Integer, ForeignKey('f_group.id'))
    exam_record = relationship('ExamRecord')


class FGroup(Base):
    __tablename__ = 'f_group'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    faculty_id = Column(Integer, ForeignKey('faculty.id'))
    student = relationship('Student')


class Faculty(Base):
    __tablename__ = 'faculty'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    staff = relationship(
        'Staff',
        secondary=staff_faculty,
        backref='parents'
    )
    group = relationship('FGroup')
    hr_record = relationship('HRRecord')


class Exam(Base):
    __tablename__ = 'exam'
    id = Column(Integer, primary_key=True)
    discipline = Column(String)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    student = relationship(
        'Student',
        secondary=exam_student,
        backref='parents'
    )
    exam_record = relationship('ExamRecord')


class ExamRecord(Base):
    __tablename__ = 'exam_record'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    exam_id = Column(Integer, ForeignKey('exam.id'),  primary_key=True)
    grade = Column(Integer)
    date = Column(Date)


class HRRecord(Base):
    __tablename__ = 'hr_record'
    staff_id = Column(Integer, ForeignKey('staff.id'), primary_key=True)
    faculty_id = Column(Integer, ForeignKey('faculty.id'),  primary_key=True)
    position = Column(String)
