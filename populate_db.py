import csv
import sqlite3 as sql
from sqlite3 import Error

def create_connection(db_name):
    conn = None
    try:
        conn = sql.connect(db_name)
        return conn
    except Error as e:
        print(e)

def create_table(conn, tbl_info):
    try:
        c = conn.cursor()
        c.execute(tbl_info)
    except Error as e:
        print(e)

def create_student(conn, info):
    insert_info = """ INSERT INTO StudentInfo(StudentID, LastName, FirstName, Age)
					  VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(insert_info, info)
    conn.commit()
    return cur.lastrowid

def create_faculty(conn, info):
    insert_info = """ INSERT INTO FacultyInfo(FacultyID, LastName, FirstName, Age)
					  VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(insert_info, info)
    conn.commit()
    return cur.lastrowid

def create_course(conn, info):
    insert_info = """ INSERT INTO CourseInfo(CourseID, CourseName)
					  VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(insert_info, info)
    conn.commit()
    return cur.lastrowid

def create_room(conn, info):
    insert_info = """ INSERT INTO RoomInfo(RoomID, BuildingName, BuildingNo, RoomNo, Length, Width, StudentCapacity)
					  VALUES(?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(insert_info, info)
    conn.commit()
    return cur.lastrowid

def create_class(conn, info):
    insert_info = """ INSERT INTO ClassInfo(CourseID, SectionNo, FacultyID, StartTime, EndTime, RoomID, Days, StudentCapacity)
					  VALUES(?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(insert_info, info)
    conn.commit()
    return cur.lastrowid

def create_schedule_entry(conn, info):
    insert_info = """ INSERT INTO ScheduleInfo(StudentID, CourseID, SectionNo, SeatNo)
					  VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(insert_info, info)
    conn.commit()
    return cur.lastrowid

def pop_table(fname, file, fun):
	conn = create_connection(fname)
	first = True

	with open(file) as f:
		reader = csv.reader(f)
		for row in reader:
			if first:
				first = False
			else:
				fun(conn, row)

	conn.close()

def create_db():
	conn = create_connection('./contact_data.db')

	student = ''' CREATE TABLE "StudentInfo" (
								"StudentID"	INTEGER NOT NULL,
								"LastName"	TEXT NOT NULL,
								"FirstName"	TEXT NOT NULL,
								"Age"	INTEGER NOT NULL
														) '''

	faculty = ''' CREATE TABLE "FacultyInfo" (
								"FacultyID"	INTEGER NOT NULL,
								"LastName"	TEXT NOT NULL,
								"FirstName"	TEXT NOT NULL,
								"Age"	INTEGER NOT NULL
														) '''

	course = ''' CREATE TABLE "CourseInfo" (
								"CourseID"	INTEGER NOT NULL,
								"CourseName"	TEXT NOT NULL
														) '''

	room = ''' CREATE TABLE "RoomInfo" (
								"RoomID"	INTEGER NOT NULL,
								"BuildingNo"	INTEGER NOT NULL,
								"BuildingName"	TEXT NOT NULL,
								"RoomNo"	INTEGER NOT NULL,
								"Length"	INTEGER NOT NULL,
								"Width"	INTEGER NOT NULL,
								"StudentCapacity"	INTEGER NOT NULL
														) '''

	classes = ''' CREATE TABLE "ClassInfo" (
								"CourseID"	INTEGER NOT NULL,
								"SectionNo"	INTEGER NOT NULL,
								"FacultyID"	INTEGER NOT NULL,
								"StartTime"	TEXT NOT NULL,
								"EndTime"	TEXT NOT NULL,
								"RoomID"	INTEGER NOT NULL,
								"Days"	INTEGER NOT NULL,
								"StudentCapacity"	INTEGER NOT NULL
														) '''

	schedule = ''' CREATE TABLE "ScheduleInfo" (
							"StudentID"	INTEGER NOT NULL,
							"CourseID"	INTEGER NOT NULL,
							"SectionNo"	INTEGER NOT NULL,
							"SeatNo"	INTEGER NOT NULL)'''
	
	contactGraph = ''' CREATE TABLE "ContactGraph"(
		"StudentID" INTEGER NOT NULL,
		"NeighborID" INTEGER NOT NULL,
		"CourseID" INTEGER NOT NULL,
		"SectionNo" INTEGER NOT NULL,
		"Distance" INTEGER NOT NULL,
		"Duration" INTEGER NOT NULL)'''
	
	create_table(conn, student)
	create_table(conn, faculty)
	create_table(conn, course)
	create_table(conn, room)
	create_table(conn, classes)
	create_table(conn, schedule)
	create_table(conn,contactGraph)
	conn.close()	

#def main():
	# first = True
	# conn = create_connection('contact_data.db')

	# with open('simulated-data/ClassInfo.csv') as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		if first:
	# 			first = False
	# 		else:
	# 			create_class(conn, row)

	# first = True
	# with open('simulated-data/CourseInfo.csv') as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		if first:
	# 			first = False
	# 		else:
	# 			create_course(conn, row)

	# first = True
	# with open('simulated-data/RoomInfo.csv') as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		if first:
	# 			first = False
	# 		else:
	# 			create_room(conn, row)

	# first = True
	# with open('simulated-data/FacultyInfo.csv') as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		if first:
	# 			first = False
	# 		else:
	# 			create_faculty(conn, row)

	# first = True
	# with open('simulated-data/StudentInfo.csv') as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		if first:
	# 			first = False
	# 		else:
	# 			create_student(conn, row)

	# first = True
	# with open('simulated-data/ScheduleInfo.csv') as f:
	# 	reader = csv.reader(f)
	# 	for row in reader:
	# 		if first:
	# 			first = False
	# 		else:
	# 			create_schedule_entry(conn, row)

