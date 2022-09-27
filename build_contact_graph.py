import csv
import sqlite3 as sql
from sqlite3 import Error
import math

def create_connection(db_name):
    conn = None
    try:
        conn = sql.connect(db_name)
        return conn
    except Error as e:
        print(e)


def get_duration_of_contact(start_time, end_time):
    conversionTime = {'8:10': 0, '9:10': 1, '10:10': 2, '11:10': 3,
                      '12:10': 4, '1:10': 5, '2:10': 6, '3:10': 7, '4:10': 8, '5:10': 9}
    return conversionTime[end_time] - conversionTime[start_time]


def get_distance_of_contact(seatNo1, seatNo2, x_num_students, adj_dist_student):
    '''room_area = length*width
    area_per_student = room_area/num_students
    adj_dist_student = area_per_student**0.5
    x_num_students = int(math.ceil(width/adj_dist_student))
    print(adj_dist_student)'''
    # y_num_students = int(math.ceil(length/adj_dist_student))
    s1_i, s1_j = (seatNo1 - 1)//x_num_students, (seatNo1 - 1) % x_num_students
    s2_i, s2_j = (seatNo2 - 1)//x_num_students, (seatNo2 - 1) % x_num_students
    # print(s1_i, s1_j, s2_i, s2_j)
    dist = ((abs(s1_i - s2_i))**2 + (abs(s1_j - s2_j))**2)**0.5
    return dist*adj_dist_student


def get_probability_of_transmission(seatNo1, seatNo2, x_num_students, adj_dist_student, start_time, end_time):
    contact_distance = get_distance_of_contact(
        seatNo1, seatNo2, x_num_students, adj_dist_student)
    contact_duration = get_duration_of_contact(start_time, end_time)

    if contact_duration > 0.25 and contact_distance < 92:
        return 100
    else:
        return 0


def create_edge(StudentId, NeighborId, ClassId, SectionNo, Distance, Duration, conn):
    cur3 = conn.cursor()
    insert_info = """ INSERT INTO ContactGraph(StudentID, NeighborID, CourseID, SectionNo, Distance,Duration)
					  VALUES(?,?,?,?,?,?) """
    cur3.execute(insert_info, (StudentId, NeighborId,
                               ClassId, SectionNo, Distance, Duration))
    conn.commit()


def add_neighbors(students_info, room_id, start_time, end_time, conn):
    cur2 = conn.cursor()
    cur2.execute(''' SELECT * FROM RoomInfo WHERE RoomID = ?''', (room_id,))
    room_info = cur2.fetchall()[0]
    length = int(room_info[4])
    width = int(room_info[5])
    room_area = length*width
    num_students = len(students_info)
    area_per_student = room_area/num_students
    adj_dist_student = area_per_student**0.5
    x_num_students = int(math.ceil(width/adj_dist_student))

    for i in range(len(students_info)):
        for j in range(len(students_info)):
            if i != j:
                #probability_of_transmission = get_probability_of_transmission(students_info[i][3], students_info[j][3], x_num_students, adj_dist_student, start_time, end_time)
                seatNo1 = students_info[i][3]
                seatNo2 = students_info[j][3]
                contact_distance = get_distance_of_contact(
                    seatNo1, seatNo2, x_num_students, adj_dist_student)
                contact_duration = get_duration_of_contact(
                    start_time, end_time)
                #print(contact_distance)
                if contact_distance <= 72:
                    create_edge(students_info[i][0], students_info[j][0], students_info[0]
                                [1], students_info[0][2], contact_distance, contact_duration, conn)


def build_graph(conn):
    cur = conn.cursor()
    cur.execute(''' SELECT * FROM ClassInfo ''')
    while(True):
        row = cur.fetchone()
        if row == None:
            break
        room_id = row[5]
        start_time = row[3]
        end_time = row[4]
        cur1 = conn.cursor()
        cur1.execute(
            ''' SELECT * FROM ScheduleInfo WHERE CourseId = ? AND SectionNo = ?''', (row[0], row[1]))
        students_info = cur1.fetchall()
        add_neighbors(students_info, room_id, start_time, end_time, conn)



'''def main():
    conn = create_connection('contact_data.db')
    print(conn)
    build_graph(conn)


main()'''
