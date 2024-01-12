from datetime import datetime
from random import randint
from faker.providers import BaseProvider
from ex_7.connect_db import session
from ex_7.models import Group, Student, Teacher, Subject, Mark
import calendar
import faker

COUNT_STUDENTS = randint(30, 50)
COUNT_GROUPS = 3
COUNT_SUBJECTS = randint(5, 8)
COUNT_TEACHERS = randint(3, 5)
MAX_COUNT_POINTS = 20

class CollegeSubjectProvider(BaseProvider):
    def college_subject(self):
        subjects_list = [ "Mathematics", "English", "Science", "History", "Geography",
            "Physics", "Chemistry", "Biology", "Computer Science", "Art",
            "Music", "Physical Education", "Literature", "Social Studies",
            "Spanish", "French", "German", "Economics", "Psychology",
            "Sociology", "Astronomy", "Philosophy", "Political Science",
            "Environmental Science", "Health Education", "Business Studies",
            "Information Technology", "Drama", "Dance", "Nutrition",
            "Ethics", "Anthropology", "Linguistics", "Graphic Design",
            "Robotics", "Statistics", "Media Studies", "Geology",
            "Home Economics", "Industrial Arts", "Mythology", "Meteorology",
            "Criminology", "Mythology", "Oceanography", "Archaeology",
            "Ethics", "Cultural Studies", "Logic", "Women's Studies"
        ]
        return self.random_element(subjects_list)

def generate_fake_data(count_students: int, count_groups: int, count_subjects: int, count_teachers: int, max_count_points: int) -> tuple():
    fake_students = []
    fake_groups = []
    fake_subjects = []
    fake_teachers = []
    fake_journal = []
    
    fake_data = faker.Faker()
    fake_data.add_provider(CollegeSubjectProvider)

    for _ in range(count_students):
        fake_students.append(fake_data.name())
    
    for _ in range(count_groups):
        fake_groups.append(fake_data.bothify(text='??-##').upper())
        
    for _ in range(count_subjects):
        fake_subjects.append(fake_data.college_subject())
        
    for _ in range(count_teachers):
        fake_teachers.append(fake_data.name())
        
    for _ in range(count_students):
        fake_marks = []
        for _ in range(randint(0, max_count_points)):
            fake_marks.append(randint(1, 12))
        fake_journal.append(fake_marks)
        
    return fake_students, fake_groups, fake_subjects, fake_teachers, fake_journal

def prepare_data(fake_students: list, fake_groups: list, fake_subjects: list, fake_teachers: list, fake_journal: list) -> tuple():
    groups = []
    for group in fake_groups:
        groups.append({ "name": group })
        
    studens = []
    for student in fake_students:
        studens.append((student, randint(1, COUNT_GROUPS)))
        
    teachers = []
    for teacher in fake_teachers:
        teachers.append((teacher, ))
        
    subjects = []
    for subject in fake_subjects:
        subjects.append((subject, randint(1, COUNT_TEACHERS)))
        
    marks_journal = []
    for index, marks in enumerate(fake_journal):
        student_id = index + 1
        for mark in marks:
            subject_id = randint(1, COUNT_SUBJECTS)
            month = randint(1, 12)
            day = randint(1, calendar.monthrange(2023, month)[1])
            mark_date = datetime(2023, month, day)
            marks_journal.append((mark, student_id, subject_id, mark_date.date()))
            
    return groups, studens, teachers, subjects, marks_journal

def insert_data_to_db(groups: list, studets: list, teachers: list, subjects: list, marks: list) -> None:
    pass

if __name__ == "__main__":
    fake_data = generate_fake_data(COUNT_STUDENTS, COUNT_GROUPS, COUNT_SUBJECTS, COUNT_TEACHERS, MAX_COUNT_POINTS)
    prepared_data = prepare_data(*fake_data)
    insert_data_to_db(*prepared_data)