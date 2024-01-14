from sqlalchemy.sql import func, desc, and_
from ex_7.connect_db import session
from ex_7.models import Student, Mark, Subject, Group, Teacher

def select_1():
    return session.query(Student.name, func.round(func.avg(Mark.mark), 2).label("mark")).select_from(Mark).join(Student).group_by(Student.id).order_by(desc("mark")).limit(5).all()

def select_2():
    return session.query(Student.name, func.round(func.avg(Mark.mark), 2).label("mark")).select_from(Student).join(Mark).group_by(Student.id).where(Mark.subject_id == 2).order_by(desc("mark")).first()

def select_3():
    return session.query(Group.code, func.round(func.avg(Mark.mark), 2).label("mark")).select_from(Group).join(Group.students).join(Student.marks).where(Mark.subject_id == 2).group_by(Group.code).all()

def select_4():
    return session.query(func.round(func.avg(Mark.mark), 2).label("mark")).select_from(Mark).first()

def select_5():
    return session.query(Subject.name.label("subject"), Teacher.name.label("teacher")).select_from(Subject).join(Subject.teacher).where(Teacher.id == 4).all()

def select_6():
    return session.query(Student.name, Group.code.label("group_code")).select_from(Student).join(Student.group).where(Student.group_id == 2).all()

def select_7():
    return session.query(Student.name, Mark.mark, Subject.name.label("subject")).select_from(Mark).join(Mark.student).join(Mark.subject).where(and_(Student.group_id == 3, Mark.subject_id == 4)).order_by(desc(Mark.mark)).all()

def select_8():
    return session.query(func.round(func.avg(Mark.mark), 2).label("mark")).select_from(Mark).join(Mark.subject).join(Subject.teacher).where(Teacher.id == 4).all()

def select_9():
    return session.query(Subject.name.label("subject"), Student.name.label("student")).select_from(Subject).join(Subject.marks).join(Mark.student).where(Student.id == 23).group_by(Subject.name, Student.name).all()

def select_10():
    return session.query(Subject.name.label("subject"), Student.name.label("student"), Teacher.name.label("teacher")).select_from(Subject).join(Subject.marks).join(Subject.teacher).join(Mark.student).where(and_(Teacher.id == 4, Student.id == 12)).group_by(Subject.name, Student.name, Teacher.name).all()

if __name__ == "__main__":
    print(select_10())