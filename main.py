import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidgetItem, QHeaderView, QTextEdit, QTextBrowser, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from homepage import Ui_MainWindow
from login import Ui_Form 

import smtplib
import urllib
import numpy as np
import mysql.connector
import cv2
import pyttsx3
import pickle
from datetime import datetime , timedelta
import time
from email.mime.text import MIMEText

# 1 Create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ugfs31SYP@", database="facerecognition")
date = datetime.utcnow()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
cursor = myconn.cursor()


class homeScreen(QMainWindow):
    def __init__(self, loginId, studentId, name, idx, timetable_data, loginTime, homePageCourse):
        super(homeScreen,self).__init__()

        self.setMinimumSize(1000,800)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(idx)
        self.ui.home_btn.setChecked(True)

        self.setWindowTitle("ICMS")

        if(idx == 0):
            self.ui.home_btn.setChecked(True)
        else:
            self.ui.noClass_message.setText("No class in 1 hr")
            self.ui.timetable_btn.setChecked(True)

        self.loginId = loginId
        self.studentId = studentId
        self.name = name
        self.loginTime = loginTime

        self.setWelcomeMessage()
        self.setLoginTime()

        self.populateLoginHistoryPage()

        header = self.ui.loginhistory_table.horizontalHeader()
        header.ResizeMode(QHeaderView.Stretch)

        header = self.ui.loginhistory_table.horizontalHeader()     
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.ui.exit_btn.clicked.connect(self.logout)
        
        #init timetable data
    
            
        self.ui.textEdit.setText(timetable_data[0])
        self.ui.textEdit_2.setText(timetable_data[1])
        self.ui.textEdit_3.setText(timetable_data[2])
        self.ui.textEdit_4.setText(timetable_data[3])
        self.ui.textEdit_5.setText(timetable_data[4])

        self.ui.textEdit_2.setReadOnly(True)
        self.ui.textEdit_3.setReadOnly(True)
        self.ui.textEdit_4.setReadOnly(True)
        self.ui.textEdit_5.setReadOnly(True)
        self.ui.textEdit.setReadOnly(True)
        
        
        if(idx == 0):
            self.load_homepage(homePageCourse)    
    
    def load_homepage(self,homePageCourse):
        
        self.ui.noClass_message.deleteLater()
        
        self.ui.home_text_Browser = QTextBrowser()
        self.ui.mail_button = QPushButton("Send to Mail")
        self.ui.mail_button.clicked.connect(self.send_email)
        
        self.ui.home_text_Browser.setOpenExternalLinks(True)
        self.ui.home_text_Browser.setReadOnly(True)
        
        self.ui.gridLayout_3.addWidget(self.ui.home_text_Browser, 0, 0, 1, 1)
        self.ui.gridLayout_3.addWidget(self.ui.mail_button)
        
        # display the related course info
        
        self.output = ""
        cursor.execute("SELECT * FROM courses WHERE course_id ='%s' ;"% (homePageCourse))
        myresult = cursor.fetchall()
        print("SELECT * FROM courses WHERE course_id ='%s' ;"% (homePageCourse))
        print(myresult)

        courseID = myresult[0][0]
        courseName = myresult[0][1]
        Address = myresult[0][2]
        
        self.output += "<h1>%s - %s</h1>" % (courseID,courseName)
        
        cursor.execute("SELECT name FROM teachers NATURAL JOIN teaches WHERE course_id ='%s';"% (homePageCourse))
        myresult = cursor.fetchall()
        
        teacher_name = myresult[0][0]
        
        self.output += "<h2>Teacher: %s</h2>" % (teacher_name)
        
        self.output += "<h2>%s</h2>" % (Address)
            
        cursor.execute("SELECT material_type, material_link FROM coursematerials WHERE course_id ='%s' ;"% (homePageCourse))
        myresult = cursor.fetchall()
        
        temp=""
        zoom=""
        msg=""
        
        for x in myresult:
            type = x[0]
            link = x[1]
            if(type=="zoom" or type =="Zoom"):
                zoom += "<p>Link : <a href=\'%s'>%s</a></p>" % (link,link)
            elif(type=="msg"):
                msg += "<p>%s</p>" % (link)
            else:
                temp+= "<p>%s: <a href=\'%s'>%s</a></p>" % (type,link,link)
                
        self.output = self.output + "<h2>Teacher's Messages</h2>" + msg
        self.output = self.output + "<h2>Zoom Meetings</h2>" + zoom
        self.output = self.output + "<h2>Additional Course Materials</h2>" + temp
        
        self.ui.home_text_Browser.setHtml(self.output)
        
    def send_email(self):
            
            # get email
            cursor.execute("SELECT email FROM students WHERE student_id =%s ;"% (self.studentId))
            myresult = cursor.fetchall()
            
            # Get the email details from the input fields
            sender = ""
            recipient = myresult[0][0]
            # SMTP server configuration
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            # Email credentials (replace with your own)
            username = 'comp3278mailbot@gmail.com'
            password = 'sctp pias vttl iwik'
            try:
                # Create a secure connection to the SMTP server
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                # Log in to the email account
                server.login(username, password)
                my_email = MIMEText(self.output, "html")
                my_email["From"] = username
                my_email["To"] = recipient
                my_email["Subject"] = "Class Info"
                # Send the email
                server.sendmail(sender, recipient, my_email.as_string())
                # Close the connection to the SMTP server
                server.quit()
                # Display a success message
                print("Email sent successfully!")
            except Exception as e:
                # Display an error message
                print("An error occurred while sending the email:", str(e))
                
        
        

    def logout(self):
        self.login = loginForm()
        self.login.show()
        self.updateLoginRecord()
        self.hide()

    def setLoginTime(self):
        time = "Login Time: " + self.loginTime
        self.ui.time.setText(time)

    def setWelcomeMessage(self):
        greeting = "Welcome, " + self.name
        self.ui.greeting.setText(greeting)

    def populateLoginHistoryPage(self):
        select = "SELECT login_id , login_time, logout_time, TIMEDIFF(logout_time, login_time)  AS Uptime FROM loginrecord WHERE student_id=%s"  % (self.studentId)

        #hide row label
        self.ui.loginhistory_table.verticalHeader().setVisible(False)

        table = QTableWidgetItem()
        table.setTextAlignment(4)

        cursor.execute(select)
        result = cursor.fetchall()

        self.ui.loginhistory_table.setRowCount(0)
        self.ui.loginhistory_table.setHorizontalHeaderLabels(['Login_id', 'Login_Time', 'Logout_Time','uptime'])

        for row_number, row_data in enumerate(result):
            self.ui.loginhistory_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.loginhistory_table.setItem(row_number,column_number,QTableWidgetItem(str(data)))




    def updateLoginRecord(self):
        update =  "UPDATE loginRecord SET logout_time=%s WHERE login_id=%s" 
        val = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.loginId)
        cursor.execute(update, val)

        myconn.commit()

    def on_home_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_timetable_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        #self.ui.stackedWidget.setCurrentWidget

    def on_loginhistory_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

class loginForm(QWidget):

    def __init__(self):
        super(loginForm,self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.login_btn.clicked.connect(self.authenticate)
        
    def authenticate(self):
        username = self.ui.username_lineEdit.text()
        print(username)


        #if username is empty
        if username == "":
            self.ui.error_message.setText("Please Enter a Username!")
            return

        select = "SELECT student_id FROM students WHERE name='%s'"  % (username)

        cursor.execute(select)
        result = cursor.fetchall()

        data = "error"

        for x in result:
            data = x

        if data == "error":
            self.ui.error_message.setText("wrong username!")
        else:
            self.ui.error_message.clear()
            self.face_login()



    def face_login(self):
        #2 Load recognize and read label from model
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("FaceRecognition/train.yml")

        labels = {"person_name": 1}
        with open("FaceRecognition/labels.pickle", "rb") as f:
            labels = pickle.load(f)
            labels = {v: k for k, v in labels.items()}

        # create text to speech
        engine = pyttsx3.init()
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 175)

        # Define camera and detect face
        face_cascade = cv2.CascadeClassifier('FaceRecognition/haarcascade/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)

        # set timer for camera
        MAX_RECOGNITION_DURATION = 10
        start_time = time.time()
        face_recognized = False

        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                print(x, w, y, h)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]
                # predict the id and confidence for faces
                id_, conf = recognizer.predict(roi_gray)

                # If the face is recognized
                if conf >= 60:
                    # print(id_)
                    # print(labels[id_])
                    font = cv2.QT_FONT_NORMAL
                    id = 0
                    id += 1
                    name = labels[id_]
                    current_name = name
                    color = (255, 0, 0)
                    stroke = 2
                    cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                    # Find the student's information in the database.
                    select = "SELECT student_id, name  FROM Students WHERE name='%s'" % (name)
                    name = cursor.execute(select)
                    result = cursor.fetchall()
                    # print(result)
                    data = "error"

                    for x in result:
                        data = x
                        
                    s_id = data[0]
                    
                    # If the student's information is not found in the database
                    if data == "error":
                        print("The student", current_name, "is NOT FOUND in the database.")

                    # If the student's information is found in the database3
                    else:

                        #fetch student class start time
                        print(s_id)
                        cmd = ("SELECT start_time, c.course_id FROM students as s, courseschedule as cs, courses as c , taking as t WHERE t.course_id = c.course_id AND t.student_id = s.student_id AND cs.course_id = c.course_id AND t.student_id =%s")%(s_id)
                        print(cmd)
                        cursor.execute(cmd)
                        
                        myresult = cursor.fetchall()
                        
                        self.idx = 1
                        
                        self.homePageCourse = "NULL"
                        
                        for x in myresult:
                            starttime = x[0]

                            #check if the student has class in 1 hr
                            
                            timediff = starttime - datetime.now()
                            
                            if((timediff <= timedelta(hours=1)) and (timediff >= timedelta(hours=0)) ):
                                
                                print("CLASS IN 1 HR")
                                self.idx = 0
                                
                                self.homePageCourse = x[1]
                        
                        # get the course data
                        cmd = ("SELECT course_id, course_name, classroom_address, start_time, end_time FROM Courses NATURAL JOIN courseschedule NATURAL JOIN taking WHERE student_id= %s")%(s_id)
                        cursor.execute(cmd)
                        myresult = cursor.fetchall()
                        
                        
                        # seperate data into days
                        self.timetable_data=["","","","",""]
   
                        for x in myresult:
                            courseID = x[0]
                            courseName = x[1]
                            Address = x[2]
                            
                            starttime = x[3].strftime('%H:%M')
                            endtime = x[4].strftime('%H:%M')
                            
                            day = x[3].strftime('%A')
                            
                            string = "%s-%s\t%s-%s\t%s\n" % (courseID, courseName, starttime, endtime, Address)
                            
                            
                            if(day == "Monday"):
                                self.timetable_data[0] += string
                            if(day == "Tuesday"):
                                self.timetable_data[1] += string
                            if(day == "Wednesday"):
                                self.timetable_data[2] += string
                            if(day == "Thursday"):
                                self.timetable_data[3] += string
                            if(day == "Friday"):
                                self.timetable_data[4] += string

                        """
                        Implement useful functions here.
                        Check the course and classroom for the student.
                            If the student has class room within one hour, the corresponding course materials
                                will be presented in the GUI.
                            if the student does not have class at the moment, the GUI presents a personal class 
                                timetable for the student.

                        """
                        # Update the data in database
                        insert =  "INSERT INTO LoginRecord (student_id, login_time) VALUES (%s,%s) "
                        currentTime = datetime.now()
                        self.loginTime = currentTime.strftime('%H:%M:%S')
                        val = (data[0], currentTime.strftime('%Y-%m-%d %H:%M:%S'),)
                        cursor.execute(insert, val)
                        self.loginId = cursor.lastrowid
                        self.studentId = data[0]
                        self.name = data[1]
                        myconn.commit()
                    
                        face_recognized = True
                        # engine.runAndWait()


                # If the face is unrecognized
                else: 
                    color = (255, 0, 0)
                    stroke = 2
                    font = cv2.QT_FONT_NORMAL
                    cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                    hello = ("Your face is not recognized")
                    print(hello)
                    engine.say(hello)
                    # engine.runAndWait()

            elapsed_time = time.time() - start_time

            if face_recognized or elapsed_time >= MAX_RECOGNITION_DURATION:
                break

            cv2.imshow('Face Login', frame)
            k = cv2.waitKey(20) & 0xff
            if k == ord('q'):
                break
                
        cap.release()
        cv2.destroyAllWindows()

        if face_recognized:
            self.show_HomeScreen()
            return data[1]

    def show_HomeScreen(self):
        self.homeScreen = homeScreen(self.loginId, self.studentId, self.name , self.idx, self.timetable_data, self.loginTime, self.homePageCourse)
        self.homeScreen.show()
        self.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss","r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)

    window = loginForm()
    window.show()

    sys.exit(app.exec())