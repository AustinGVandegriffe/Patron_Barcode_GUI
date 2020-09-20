# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Barcode_GUI\.\form_state.ui',
# licensing of '.\Barcode_GUI\.\form_state.ui' applies.
#
# Created: Sun Jul 14 01:41:17 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

###############################################################
# ADDED 2019-07-12 BY AUSTIN VANDEGRIFFE FROM https://stackoverflow.com/a/53237231
# docs: https://srinikom.github.io/pyside-docs/PySide/QtGui/index.html
import sys, os, sqlite3, datetime, time
# time.strftime("%Y-%m-%d %H:%M:%S")
# datetime.datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
import PySide2

conn = sqlite3.connect("./patron_barcode_record.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS barcodes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entry_date STRING,
                worker_name STRING,
                id_type STRING,
                id_input STRING,
                patron_id STRING,
                login_barcode STRING
            )""")

conn.commit()

c.execute("SELECT DISTINCT entry_date FROM barcodes;")

today = datetime.datetime.now()
dates = c.fetchall()
for day in dates:
    if (today - datetime.datetime.strptime(day[0], "%Y-%m-%d %H:%M:%S")).days >= 14:
        print(day)
        c.execute(f'DELETE FROM barcodes WHERE entry_date="{day[0]}"')
conn.commit()

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
###############################################################

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):

        self.date = time.strftime("%Y-%m-%d %H:%M:%S")

        Form.setObjectName("Form")
        Form.resize(522, 440)

        self.label_date = QtWidgets.QLabel(Form)
        self.label_date.setGeometry(QtCore.QRect(30, 30, 211, 16))
        self.label_date.setObjectName("label_date")
        self.todays_date = QtWidgets.QLabel(Form)
        self.todays_date.setGeometry(QtCore.QRect(250, 30, 211, 16))
        self.todays_date.setObjectName("todays_date")

        self.label_worker = QtWidgets.QLabel(Form)
        self.label_worker.setGeometry(QtCore.QRect(30, 70, 211, 16))
        self.label_worker.setObjectName("label_worker")
        self.dropdown_worker = QtWidgets.QComboBox(Form)
        self.dropdown_worker.setGeometry(QtCore.QRect(249, 70, 211, 31))
        self.dropdown_worker.setObjectName("dropdown_worker")
        self.dropdown_worker.addItem("")

        self.label_id_type = QtWidgets.QLabel(Form)
        self.label_id_type.setGeometry(QtCore.QRect(30, 135, 211, 21))
        self.label_id_type.setObjectName("label_id_type")
        self.dropdown_id_type = QtWidgets.QComboBox(Form)
        self.dropdown_id_type.setGeometry(QtCore.QRect(250, 135, 211, 31))
        self.dropdown_id_type.setObjectName("dropdown_id_type")

        self.label_state = QtWidgets.QLabel(Form)
        self.label_state.setGeometry(QtCore.QRect(30, 180, 211, 16))
        self.label_state.setObjectName("label_state")
        self.dropdown_states = QtWidgets.QComboBox(Form)
        self.dropdown_states.setGeometry(QtCore.QRect(250, 180, 211, 31))
        self.dropdown_states.setObjectName("dropdown_states")
        self.dropdown_states.addItem("")

        self.label_id_input = QtWidgets.QLabel(Form)
        self.label_id_input.setGeometry(QtCore.QRect(30, 248, 211, 16))
        self.label_id_input.setObjectName("label_id_input")
        self.input_id = QtWidgets.QLineEdit(Form)
        self.input_id.setGeometry(QtCore.QRect(250, 248, 211, 31))
        self.input_id.setObjectName("input_id")

        self.input_login_barcode = QtWidgets.QLineEdit(Form)
        self.input_login_barcode.setGeometry(QtCore.QRect(250, 320, 211, 31))
        self.input_login_barcode.setObjectName("input_login_barcode")
        self.label_login_barcode = QtWidgets.QLabel(Form)
        self.label_login_barcode.setGeometry(QtCore.QRect(30, 320, 211, 16))
        self.label_login_barcode.setObjectName("label_login_barcode")

        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setGeometry(QtCore.QRect(430, 400, 71, 31))
        self.submit.setAutoDefault(True)
        self.submit.setDefault(True)
        self.submit.setObjectName("submit")


        self.label_worker.setBuddy(self.label_worker)

        # Non State Popups
        self.label_country = QtWidgets.QLabel(Form)
        self.label_country.setGeometry(QtCore.QRect(30, 180, 211, 16))
        self.label_country.setObjectName("label_country")
        self.label_country.setVisible(False)
        self.dropdown_country = QtWidgets.QComboBox(Form)
        self.dropdown_country.setGeometry(QtCore.QRect(250, 180, 211, 31))
        self.dropdown_country.setObjectName("dropdown_country")
        self.dropdown_country.setVisible(False)

        self.label_other = QtWidgets.QLabel(Form)
        self.label_other.setGeometry(QtCore.QRect(30, 180, 211, 16))
        self.label_other.setObjectName("label_other")
        self.label_other.setVisible(False)
        self.input_other = QtWidgets.QLineEdit(Form)
        self.input_other.setGeometry(QtCore.QRect(250, 180, 211, 31))
        self.input_other.setObjectName("input_other")
        self.input_other.setVisible(False)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def id_type_clear(self):
        self.label_state.setVisible(False)
        self.dropdown_states.setVisible(False)
        self.label_country.setVisible(False)
        self.dropdown_country.setVisible(False)
        self.label_other.setVisible(False)
        self.input_other.setVisible(False)

    def set_id_type(self):
        self.id_type_clear()
        if "DL" in self.dropdown_id_type.currentText():
            self.label_state.setVisible(True)
            self.dropdown_states.setVisible(True)
        elif "PP" in self.dropdown_id_type.currentText():
            self.label_country.setVisible(True)
            self.dropdown_country.setVisible(True)
        else:
            self.label_other.setVisible(True)
            self.input_other.setVisible(True)

    def rec_and_quit(self):
        tmp = ""
        if "DL" in self.dropdown_id_type.currentText():
            tmp = self.dropdown_states.currentText()
        elif "PP" in self.dropdown_id_type.currentText():
            tmp = self.dropdown_country.currentText()
        if self.dropdown_id_type.currentText() == "Other":
            tmp = self.input_other.text()

        c.execute('INSERT INTO barcodes (entry_date, worker_name, id_type, id_input, patron_id, login_barcode) VALUES ("{}","{}","{}","{}","{}","{}");'.format(
                self.date, self.dropdown_worker.currentText(), self.dropdown_id_type.currentText(), tmp, self.input_id.text(), self.input_login_barcode.text()
            )
        )

        print("Submitted...")
        
        conn.commit()
        sys.exit()


    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        
        self.label_date.setText(QtWidgets.QApplication.translate("Form", "Date", None, -1))
        self.todays_date.setText(QtWidgets.QApplication.translate("Form", f"{self.date}", None, -1))

        self.label_worker.setText(QtWidgets.QApplication.translate("Form", "Worker ID:", None, -1))
        with open("employee_names.csv","r") as fin:
            inpt = fin.readlines()
            self.dropdown_worker.clear()
            self.dropdown_worker.addItem("")
            self.dropdown_worker.addItems(sorted([x.replace("\n","") for x in inpt[1:]]))

        self.label_id_type.setText(QtWidgets.QApplication.translate("Form", "Patron ID Type:", None, -1))
        self.dropdown_id_type.clear()
        self.dropdown_id_type.addItems(["Driver\'s Liscense (DL)", "Passport (PP)", "Other"])

        self.label_state.setText(QtWidgets.QApplication.translate("Form", "State:", None, -1))
        with open("states.txt","r") as fin:
            self.dropdown_states.clear()
            self.dropdown_states.addItems([x.replace('\n','') for x in fin.readlines()])

        self.label_country.setText(QtWidgets.QApplication.translate("Form", "Country:", None, -1))
        with open("countries.txt","r") as fin:
            self.dropdown_country.clear()
            self.dropdown_country.addItems([x.replace('\n','') for x in fin.readlines()])

        self.label_other.setText(QtWidgets.QApplication.translate("Form", "Other:", None, -1))

        self.label_login_barcode.setText(QtWidgets.QApplication.translate("Form", "Login Barcode:", None, -1))
        self.label_id_input.setText(QtWidgets.QApplication.translate("Form", "ID Input:", None, -1))

        self.submit.setText(QtWidgets.QApplication.translate("Form", "Submit", None, -1))


        self.dropdown_id_type.currentTextChanged.connect(self.set_id_type)
        self.submit.clicked.connect(self.rec_and_quit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

