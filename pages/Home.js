import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { DropzoneArea } from 'material-ui-dropzone';
import 'fontsource-roboto';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import ButtonAppBar from './buttonAppBar.js';

import '../App.css';

class Home extends Component{
	constructor(props) {
		super(props);
		this.state = {
			files: [],
			text: "Run ConTrace"
		};
	}
	handleChange(files) {
		this.setState({
			files: files
		});
	}
	
	changeText = (text) => {
		this.setState({ text });
	}
	
	fileUploader1 = (files) => {
		const formData = new FormData();

		const file = files[0];
		formData.append("file", file);

		fetch("/student_info", {
			method: "POST",
			body: formData,
		});
	}

	fileUploader2 = (files) => {
		const formData = new FormData();

		const file = files[0];
		formData.append("file", file);

		fetch("/faculty_info", {
			method: "POST",
			body: formData,
		});
	}

	fileUploader3 = (files) => {
		const formData = new FormData();

		const file = files[0];
		formData.append("file", file);

		fetch("/course_info", {
			method: "POST",
			body: formData,
		});
	}

	fileUploader4 = (files) => {
		const formData = new FormData();

		const file = files[0];
		formData.append("file", file);

		fetch("/room_info", {
			method: "POST",
			body: formData,
		});
	}

	fileUploader5 = (files) => {
		const formData = new FormData();

		const file = files[0];
		formData.append("file", file);

		fetch("/class_info", {
			method: "POST",
			body: formData,
		});
	}

	fileUploader6 = (files) => {
		const formData = new FormData();

		const file = files[0];
		formData.append("file", file);

		fetch("/schedule_info", {
			method: "POST",
			body: formData,
		});
	}
	fileUploader7 = (files) => {
		const formData = new FormData();

		const file = files[0];
		formData.append("file", file);

		fetch("/infected_students", {
			method: "POST",
			body: formData,
		});
	}
	buildGraph = () => {
		this.changeText("Loading...");
		fetch("/build_graph", {
			method: "GET",
		}).then(
			response => response.json()
		  ).then(data => console.log(data));
		this.changeText("Done!");
	}
	
	render() {
		const { text } = this.state
		return(
		<div className = "Home">
			<div>
			<ButtonAppBar heading={`Upload`}/>
			</div>
		  <h1><center>Submit Files</center></h1>
		  	<DropzoneArea
			acceptedFiles={[".csv, text/csv, application/vnd.ms-excel, application/csv, text/x-csv, application/x-csv, text/comma-separated-values, text/x-comma-separated-values"]}
			onChange={this.handleChange.bind(this)}
			showFileNames
			dropzoneText="Upload StudentInfo(StudentId,LastName,FirstName)"
			showAlerts={false}
			filesLimit={1}
			onDrop={this.fileUploader1}/>
			<br/>
			<DropzoneArea
			acceptedFiles={[".csv, text/csv, application/vnd.ms-excel, application/csv, text/x-csv, application/x-csv, text/comma-separated-values, text/x-comma-separated-values"]}
			onChange={this.handleChange.bind(this)}
			showFileNames
			dropzoneText="Upload FacultyInfo(FacultyId,LastName,FirstName)"
			showAlerts={false}
			filesLimit={1}
			onDrop={this.fileUploader2}/>
			<br/>
			<DropzoneArea
			acceptedFiles={[".csv, text/csv, application/vnd.ms-excel, application/csv, text/x-csv, application/x-csv, text/comma-separated-values, text/x-comma-separated-values"]}
			onChange={this.handleChange.bind(this)}
			showFileNames
			dropzoneText="Upload CourseInfo(CourseId,CourseName)"
			showAlerts={false}
			filesLimit={1}
			onDrop={this.fileUploader3}/>
			<br/>
			<DropzoneArea
			acceptedFiles={[".csv, text/csv, application/vnd.ms-excel, application/csv, text/x-csv, application/x-csv, text/comma-separated-values, text/x-comma-separated-values"]}
			onChange={this.handleChange.bind(this)}
			showFileNames
			dropzoneText="Upload RoomInfo(RoomId,BuildingName,RoomNo,Length,Width,StudentCapacity)"
			showAlerts={false}
			filesLimit={1}
			onDrop={this.fileUploader4}/>
			<br/>
			<DropzoneArea
			acceptedFiles={[".csv, text/csv, application/vnd.ms-excel, application/csv, text/x-csv, application/x-csv, text/comma-separated-values, text/x-comma-separated-values"]}
			onChange={this.handleChange.bind(this)}
			showFileNames
			dropzoneText="Upload ClassInfo(CourseId,SectionNo,FacultyId,startTime,endTime,RoomId,m,t,w,r,f,StudentCapacity)"
			showAlerts={false}
			filesLimit={1}
			onDrop={this.fileUploader5}/>
			<br/>
			<DropzoneArea
			acceptedFiles={[".csv, text/csv, application/vnd.ms-excel, application/csv, text/x-csv, application/x-csv, text/comma-separated-values, text/x-comma-separated-values"]}
			onChange={this.handleChange.bind(this)}
			showFileNames
			dropzoneText="Upload ScheduleInfo(StudentId,CourseId,SectionNo,SeatNo)"
			showAlerts={false}
			filesLimit={1}
			onDrop={this.fileUploader6}/>
			<br/>
			<DropzoneArea
			acceptedFiles={[".csv, text/csv, application/vnd.ms-excel, application/csv, text/x-csv, application/x-csv, text/comma-separated-values, text/x-comma-separated-values"]}
			onChange={this.handleChange.bind(this)}
			showFileNames
			dropzoneText="Upload InfectedStudents(StudentId,Year,Day,Month,Time)"
			showAlerts={false}
			filesLimit={1}
			onDrop={this.fileUploader7}/>
			<br/>
			<center><Button onClick={ this.buildGraph } variant="contained" color="primary">
				{text}
			</Button></center>
			</div>
		);
	}
}

export default Home;