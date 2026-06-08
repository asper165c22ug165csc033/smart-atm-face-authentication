import os
import random
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLineEdit


from email.mime.audio import MIMEAudio
from pydub import AudioSegment
from pydub.generators import Sine

from face import Ui_Form31

class Ui_Form4(object):
    def setupUi(self, Form4):
        Form4.setObjectName("Form4")
        Form4.resize(801, 618)
        self.label = QtWidgets.QLabel(Form4)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("33.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form4)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(13,106,121); background-color: rgb(131,238,255)")
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Form4)
        self.lineEdit.setGeometry(QtCore.QRect(450, 190, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_6 = QtWidgets.QLineEdit(Form4)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 350, 681, 51))
        self.lineEdit_6.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(255,255,255,255);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "paddin-bottom:7px;\n"
                                      "font: 16pt \"MS Shell Dlg 2\";\n"
                                      "")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.label_4 = QtWidgets.QLabel(Form4)
        self.label_4.setGeometry(QtCore.QRect(70, 190, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255,255,255);")
        self.label_4.setObjectName("label_4")

        self.timer_label = QtWidgets.QLabel(Form4)
        self.timer_label.setGeometry(QtCore.QRect(60, 410, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.timer_label.setFont(font)
        self.timer_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.timer_label.setObjectName("timer_label")
        self.timer_label.hide()  # Initially hide the timer label

        # Set initial text for the timer label
        self.timer_seconds = 120  # 2 minutes
        self.update_timer_label()

        # Create a QTimer object
        self.timer = QtCore.QTimer(Form4)
        self.timer.timeout.connect(self.update_timer)

        self.pushButton = QtWidgets.QPushButton(Form4)
        self.pushButton.setGeometry(QtCore.QRect(500, 500, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:30px;\n"
"background-color: rgb(140,120,120);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.next_page)

        self.pushButton2 = QtWidgets.QPushButton(Form4)
        self.pushButton2.setGeometry(QtCore.QRect(110, 500, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("border-radius:30px;\n"
                                      "background-color: rgb(140,120,120);")
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(self.mail)

        self.retranslateUi(Form4)
        QtCore.QMetaObject.connectSlotsByName(Form4)

    def retranslateUi(self, Form4):
        _translate = QtCore.QCoreApplication.translate
        Form4.setWindowTitle(_translate("Form",   "Form"))
        self.label_2.setText(_translate("Form", "OTP VERIFICATION "))
        self.label_4.setText(_translate("Form", "ENTER OTP "))
        self.pushButton2.setText(_translate("Form", "GENERATE OTP"))
        self.pushButton.setText(_translate("Form", "OK"))

    def next_page(self):
        print("hello")
        a=self.lineEdit.text()
        otp = ['23641', '78965', '78954', '85214', '41257','41584','58417','52145']
        if a in otp:
            print("User athenticated successfully. Proceed to the next step")
            self.lineEdit_6.setText("User authenticated successfully. Proceed to the next step")
            self.timer.stop()  # Stop the existing timer, if any
            self.timer_label.hide()

            self.Form31 = QtWidgets.QMainWindow()
            self.Ui = Ui_Form31()
            self.Ui.setupUi(self.Form31)
            self.Form31.show()

        else:
            print("Wrong OTP")
            self.lineEdit_6.setText("Wrong OTP")




    def update_timer(self):
        self.timer_seconds -= 1
        self.update_timer_label()

        if self.timer_seconds == 0:
            self.timer.stop()
            self.lineEdit_6.setText("Time expired. Please generate a new OTP.")
            self.timer_label.hide()  # Hide the timer label when time expires

    def update_timer_label(self):
        minutes = self.timer_seconds // 60
        seconds = self.timer_seconds % 60
        self.timer_label.setText(f"Time remaining: {minutes:02}:{seconds:02}")

    def mail(self):

            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            import smtplib
            import random


            strFrom = 'keerthana4117@gmail.com'
            strTo = 'keerthana4117@gmail.com'

            # Create the root message and fill in the from, to, and subject headers
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = 'subject information sending from software,user editable'
            msgRoot['From'] = strFrom
            msgRoot['To'] = strTo
            msgRoot.preamble = 'This is a multi-part message in MIME format.'

            msgAlternative = MIMEMultipart('alternative')

            msgRoot.attach(msgAlternative)

            mail_message_Text = MIMEText('The OTP for authentication is sent as an attachment ')

            msgAlternative.attach(mail_message_Text)

            # Attach a random audio file from the "otp" folder
            audio_folder = 'otp'
            audio_files = [f for f in os.listdir(audio_folder) if
                           f.endswith('.mp3')]  # Adjust the file extension if needed
            if audio_files:
                random_audio_file = random.choice(audio_files)
                audio_path = os.path.join(audio_folder, random_audio_file)

                with open(audio_path, 'rb') as audio_file:
                    audio_msg = MIMEAudio(audio_file.read(), _subtype='mp3', name=random_audio_file)

                msgRoot.attach(audio_msg)

            smtp = smtplib.SMTP('smtp.gmail.com', 587)

            smtp.starttls()

            smtp.login('keerthana4117@gmail.com', 'lwas bqvr slei snti')

            print("mail id and password correct")

            smtp.sendmail(strFrom, strTo, msgRoot.as_string())

            print("mail sent")
            self.lineEdit_6.setText("OTP is sent to mail successfully. Enter the OTP before time expires")
            self.timer_label.show()  # Show the timer label after sending OTP
            self.timer.start(1000)

            smtp.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form4 = QtWidgets.QWidget()
    ui = Ui_Form4()
    ui.setupUi(Form4)
    Form4.show()
    sys.exit(app.exec_())
