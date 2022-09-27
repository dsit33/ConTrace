import math
import sqlite3 as sql
from sqlite3 import Error

InfectedList = [{'ID': 4, 'TimeOfInfection': 't Apr 20 10:38:36 2021'}, {
    'ID': 2, 'TimeOfInfection': 'w Apr 21 12:38:36 2021'}, {'ID': 3, 'TimeOfInfection': 'r Apr 23 4:38:36 2021'}]

days = ['m', 't', 'w', 'r', 'f']
days_convert = {'m': 1, 't': 2, 'w': 3, 'r': 4, 'f': 5}

StudentsProbOfInfection = {}
for student_id in range(0, 5000):
    StudentsProbOfInfection[student_id] = 0


def getDays1(num):
    gate = 1
    arr = []
    for i in days[::-1]:
        res = num & gate
        if res == 1:
            arr.append(i)
        num >> 1
    return arr


def create_connection(db_name):
    conn = None
    try:
        conn = sql.connect(db_name)
        return conn
    except Error as e:
        print(e)


def get_class_info(course_id, section_no, conn):
    cur = conn.cursor()
    cur.execute(''' SELECT startTime,Days FROM ClassInfo WHERE CourseId = ? AND SectionNo = ?''',
                (course_id, section_no))
    res = cur.fetchone()
    return res


def get_classes(student_id, conn):
    cur = conn.cursor()
    cur.execute(
        ''' SELECT CourseId,SectionNo FROM ScheduleInfo WHERE StudentID = ?''', (student_id,))
    classes = cur.fetchall()

    return classes


def get_infected_neighbors1(student_id, course_id, section_no, conn):
    cur = conn.cursor()
    cur.execute(''' SELECT NeighborId,Distance,Duration FROM ContactGraph WHERE StudentId = ? AND CourseId = ? AND SectionNo = ? ''',
                (student_id, course_id, section_no))
    return cur.fetchall()


def isClassAfterInfected(student_timeOfInfection, day_num, start_time):
    class_days = getDays1(day_num)
    date_time = student_timeOfInfection.split()
    day = date_time[0]
    time_infected = date_time[3].split(':')
    time_min_infection = int(
        time_infected[0])*60 + int(time_infected[1])
    time_class = start_time.split(':')
    time_min_class = int(time_class[0])*60 + int(time_class[1])
    if time_min_infection >= time_min_class:
        for d in class_days:
            if days_convert[d] >= days_convert[day]:
                return True
    return False


def CalculateProb(distance, duration):
    max_duration = 2.0  # in hours

    if (distance < 12):
        return 1.0
    if (distance < 24):
        return 0.9 + (duration / max_duration) / 10
    if (distance < 36):
        return 0.8 + (duration / max_duration) / 10
    if (distance < 48):
        return 0.7 + (duration / max_duration) / 10
    if (distance < 60):
        return 0.65 + (duration / max_duration) / 10
    if (distance < 72):
        return .60 + (duration / max_duration) / 10

    return 0


def DirectContactTracing(InfectedList, conn):
    for student in InfectedList:
        StudentsProbOfInfection[student['ID']] = 100
        classes = get_classes(student['ID'], conn)
        for c in classes:
            course_id = c[0]
            section_no = c[1]
            class_info = get_class_info(course_id, section_no, conn)
            days = class_info[1]
            start_time = class_info[0]
            if isClassAfterInfected(student['TimeOfInfection'], days, start_time):
                infected_neighbors = get_infected_neighbors1(
                    student['ID'], course_id, section_no, conn)
                for n in infected_neighbors:
                    StudentsProbOfInfection[n[0]] = max(
                        StudentsProbOfInfection[n[0]], CalculateProb(n[1], n[2]))
    print(StudentsProbOfInfection)
    #print([(i, StudentsProbOfInfection[i]) for i in StudentsProbOfInfection if StudentsProbOfInfection[i] > 0])


#DirectContactTracing(InfectedList, create_connection('contact_data.db'))
