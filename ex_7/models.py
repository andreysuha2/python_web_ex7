from typing import List
from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(5), nullable=True)
    students: Mapped[List["Student"]] = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)
    group: Mapped["Group"] = relationship("Group", back_populates="students")
    marks: Mapped[List["Mark"]] = relationship("Mark", back_populates="student")
    
class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    subjects: Mapped[List["Subject"]] = relationship("Subject", back_populates="teacher")
    
class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String[50], nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id", ondelete="CASCADE"), nullable=False)
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="subjects")
    marks: Mapped[List["Mark"]] = relationship("Mark", back_populates="subject")

class Mark(Base):
    __tablename__ = "marks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    student: Mapped["Student"] = relationship("Student", back_populates="marks", foreign_keys=[student_id])
    subject: Mapped["Subject"] = relationship("Subject", back_populates="marks", foreign_keys=[subject_id])
    
    