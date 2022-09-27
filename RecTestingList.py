import sqlite3 as sql
from sqlite3 import Error
from IndirectContactTracing import *


class StudentInfo:
    def __init__(self, student_id, prob_of_infection, degree, age, tier):
        self.student_id = student_id
        self.prob_of_infection = prob_of_infection
        self.degree = degree
        self.age = age
        self.tier = tier

    def __repr__(self):
        return '(sid: {}, tier: {}, degree: {}, age: {})'.format(
            self.student_id, self.tier, self.degree, self.age)

    def __str__(self):
        return '(sid: {}, tier: {}, degree: {}, age: {})'.format(
            self.student_id, self.tier, self.degree, self.age)

    """ def __eq__(self, other):
        if self.tier == other.tier:
            
    def __lt__(self, other):
        if self.tier == other.tier:
            if self.degree == other.degree:
                if self.age == other.age:
                    return 0
                return self.age < other.age
            return self.degree < other.degree
        return self.tier < other.tier """

    def __cmp__(self, other):
        if self.tier < other.tier:
            return True
        elif self.tier == other.tier:
            if self.degree < other.degree:
                return True
            elif self.degree == other.degree:
                if self.age < other.age:
                    return True
                else:
                    return False
            else:
                return False

        else:
            return False


def get_degree(student_id, conn):
    cur = conn.cursor()
    cur.execute(
        ''' SELECT COUNT(NeighborId) FROM ContactGraph WHERE StudentId = ? GROUP BY StudentId''', (student_id,))
    return cur.fetchone()


def get_age(student_id, conn):
    cur = conn.cursor()
    cur.execute(
        ''' SELECT Age FROM StudentInfo WHERE StudentId = ?''', (student_id,))
    return cur.fetchone()


def get_tier(prob_of_infection):

    high = range(70, 101)
    medium = range(35, 70)
    low = range(15, 35)

    if prob_of_infection*100 in high:
        return 3
    if prob_of_infection*100 in medium:
        return 2
    if prob_of_infection*100 in low:
        return 1

    return 0

# def in_degree_infected()


def testing_rec_lists(student_nodes, conn):
    student_list = []
    for student_id in student_nodes:
        tier = get_tier(student_nodes[student_id].prob_of_infection)
        degree = get_degree(student_id, conn)
        age = get_age(student_id, conn)
        student_list.append(StudentInfo(
            student_id, student_nodes[student_id].prob_of_infection, degree, age, tier))
    student_list = sorted(
        student_list, key=lambda x: (x.tier, x.degree, x.age), reverse=True)
    return student_list


def check_degree(conn):
    cur = conn.cursor()
    cur.execute(
        ''' SELECT StudentId,NeighborId FROM ContactGraph WHERE StudentId = ? ''', (0,))
    return cur.fetchall()


conn = create_connection('contact_data.db')
# print(get_degree(conn))
# print(check_degree(conn))
start = time.time()
print("Potentially Infected Individuals: ", end='')
student_nodes = IndirectContactTracing(InfectedList, 3, conn)
print(student_nodes)
stop = time.time()
print("Execution Time: %d seconds" % (stop - start))

print(testing_rec_lists(student_nodes, conn))

conn.close()
