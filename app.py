import time
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS
import logging
import os
import shutil
from populate_db import *
from build_contact_graph import *
from IndirectContactTracing import *

app = Flask(__name__)
app.config['UPLOAD_PATH'] = './resources'
CORS(app)

#if os.path.exists('./resources'):
#	shutil.rmtree('./resources')
#os.makedirs('./resources')

#if os.path.exists('./contact_data.db'):
#	os.remove('./contact_data.db')
#create_db()

@app.route('/student_info', methods=['GET', 'POST'])
def student_upload():
	if request.method == 'POST':
		print("Saving file")
		f = request.files['file']
		path = app.config['UPLOAD_PATH'] + '/StudentInfo.csv'
		f.save(path)

		pop_table('contact_data.db', path, create_student)
		print('Finished populating students')
		return "test"
		
@app.route('/faculty_info', methods=['GET', 'POST'])
def faculty_upload():
	if request.method == 'POST':
		print("Saving file")
		f = request.files['file']
		path = app.config['UPLOAD_PATH'] + '/FacultyInfo.csv'
		f.save(path)
		pop_table('contact_data.db', path, create_faculty)
		return "test"

@app.route('/course_info', methods=['GET', 'POST'])
def course_upload():
	if request.method == 'POST':
		print("Saving file")
		f = request.files['file']
		path = app.config['UPLOAD_PATH'] + '/CourseInfo.csv'
		f.save(path)
		pop_table('contact_data.db', path, create_course)
		return "test"

@app.route('/room_info', methods=['GET', 'POST'])
def room_upload():
	if request.method == 'POST':
		print("Saving file")
		f = request.files['file']
		path = app.config['UPLOAD_PATH'] + '/RoomInfo.csv'
		f.save(path)
		pop_table('contact_data.db', path, create_room)
		return "test"

@app.route('/class_info', methods=['GET', 'POST'])
def class_upload():
	if request.method == 'POST':
		print("Saving file")
		f = request.files['file']
		path = app.config['UPLOAD_PATH'] + '/ClassInfo.csv'
		f.save(path)
		pop_table('contact_data.db', path, create_class)
		return "test"

@app.route('/schedule_info', methods=['GET', 'POST'])
def schedule_upload():
	if request.method == 'POST':
		print("Saving file")
		f = request.files['file']
		path = app.config['UPLOAD_PATH'] + '/ScheduleInfo.csv'
		f.save(path)
		pop_table('contact_data.db', path, create_schedule_entry)
		return "test"

@app.route('/infected_students', methods=['GET', 'POST'])
def infected_upload():
	if request.method == 'POST':
		print("Saving file")
		f = request.files['file']
		path = app.config['UPLOAD_PATH'] + '/InfectedStudents.csv'
		f.save(path)
		return "test"

@app.route('/build_graph', methods=['GET', 'POST'])
def flask_build_graph():
	if request.method == 'GET':
		print("Building graph")
		conn = create_connection('./contact_data.db')
		#build_graph(conn)
		InfectedList = parse_infected(app.config['UPLOAD_PATH'] + '/InfectedStudents.csv')
		student_nodes = IndirectContactTracing(InfectedList, 3, conn)
		return jsonify(student_nodes)


CORS(app, expose_headers = 'Authorization')