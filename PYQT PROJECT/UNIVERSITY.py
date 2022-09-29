import MONGODBSAGAMOCDO
import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


conn=pymongo.MongoClient()
DATADB=conn.UNIVERSITY

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ident = QtWidgets.QLabel(self.centralwidget)
        self.ident.setGeometry(QtCore.QRect(40, 40, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ident.setFont(font)
        self.ident.setObjectName("ident")
        self.gvari = QtWidgets.QLabel(self.centralwidget)
        self.gvari.setGeometry(QtCore.QRect(40, 110, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.gvari.setFont(font)
        self.gvari.setObjectName("gvari")
        self.saxeli = QtWidgets.QLabel(self.centralwidget)
        self.saxeli.setGeometry(QtCore.QRect(40, 180, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.saxeli.setFont(font)
        self.saxeli.setObjectName("saxeli")
        self.sagani = QtWidgets.QLabel(self.centralwidget)
        self.sagani.setGeometry(QtCore.QRect(40, 260, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sagani.setFont(font)
        self.sagani.setObjectName("sagani")
        self.shepaseba = QtWidgets.QLabel(self.centralwidget)
        self.shepaseba.setGeometry(QtCore.QRect(40, 330, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shepaseba.setFont(font)
        self.shepaseba.setObjectName("shepaseba")
        self.yvelachanawb = QtWidgets.QPushButton(self.centralwidget)
        self.yvelachanawb.setGeometry(QtCore.QRect(540, 40, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yvelachanawb.setFont(font)
        self.yvelachanawb.setObjectName("yvelachanawb")
        self.dzebnab = QtWidgets.QPushButton(self.centralwidget)
        self.dzebnab.setGeometry(QtCore.QRect(540, 90, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dzebnab.setFont(font)
        self.dzebnab.setObjectName("dzebnab")
        self.ganaxlebab = QtWidgets.QPushButton(self.centralwidget)
        self.ganaxlebab.setGeometry(QtCore.QRect(540, 140, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ganaxlebab.setFont(font)
        self.ganaxlebab.setObjectName("ganaxlebab")
        self.washlab = QtWidgets.QPushButton(self.centralwidget)
        self.washlab.setGeometry(QtCore.QRect(540, 190, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.washlab.setFont(font)
        self.washlab.setObjectName("washlab")
        self.chawerabutton = QtWidgets.QPushButton(self.centralwidget)
        self.chawerabutton.setGeometry(QtCore.QRect(200, 420, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chawerabutton.setFont(font)
        self.chawerabutton.setObjectName("chawerabutton")
        self.daxurvab = QtWidgets.QPushButton(self.centralwidget)
        self.daxurvab.setGeometry(QtCore.QRect(680, 480, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.daxurvab.setFont(font)
        self.daxurvab.setObjectName("daxurvab")
        self.identtext = QtWidgets.QLineEdit(self.centralwidget)
        self.identtext.setGeometry(QtCore.QRect(200, 40, 251, 41))
        self.identtext.setObjectName("identtext")
        self.gvaritext = QtWidgets.QLineEdit(self.centralwidget)
        self.gvaritext.setGeometry(QtCore.QRect(200, 120, 251, 41))
        self.gvaritext.setObjectName("gvaritext")
        self.saxelitext = QtWidgets.QLineEdit(self.centralwidget)
        self.saxelitext.setGeometry(QtCore.QRect(200, 190, 251, 41))
        self.saxelitext.setObjectName("saxelitext")
        self.saganitext = QtWidgets.QLineEdit(self.centralwidget)
        self.saganitext.setGeometry(QtCore.QRect(200, 270, 251, 41))
        self.saganitext.setObjectName("saganitext")
        self.shepasebatext = QtWidgets.QLineEdit(self.centralwidget)
        self.shepasebatext.setGeometry(QtCore.QRect(200, 340, 251, 41))
        self.shepasebatext.setObjectName("shepasebatext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.dzebnab.clicked.connect(self.find)
        self.ganaxlebab.clicked.connect(self.Update_data)
        self.yvelachanawb.clicked.connect(self.DATABASE_UPLOAD)
        self.washlab.clicked.connect(self.delete_doc)
        self.chawerabutton.clicked.connect(self.insert_doc)
        self.daxurvab.clicked.connect(self.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ident.setText(_translate("MainWindow", " ID"))
        self.gvari.setText(_translate("MainWindow", "  Surname "))
        self.saxeli.setText(_translate("MainWindow", " Name"))
        self.sagani.setText(_translate("MainWindow", " Subject"))
        self.shepaseba.setText(_translate("MainWindow", " Assessment"))
        self.yvelachanawb.setText(_translate("MainWindow", "Make all the entries"))
        self.dzebnab.setText(_translate("MainWindow", "Search"))
        self.ganaxlebab.setText(_translate("MainWindow", "Update"))
        self.washlab.setText(_translate("MainWindow", "Delete"))
        self.chawerabutton.setText(_translate("MainWindow", "Record"))
        self.daxurvab.setText(_translate("MainWindow", "close"))

    def  find(self):
        sax=self.saxelitext.text()
        gvar=self.gvaritext.text()
        ident=self.identtext.text()
        sagan=self.saganitext.text()
        shepas=self.shepasebatext.text()
        if ident!="":
                Name=DATADB.students.find({"_id":int(ident)})
                for person in Name:
                    print(person)
        elif sax!="":
                print(sax)
                Name=DATADB.students.find({"first_name":sax})
                for person in Name:
                    print(person)
        elif gvar!="":
                print(gvar)
                Name=DATADB.students.find({"last_name":gvar})
                for person in Name:
                    print(person)
        elif sagan!="":
                Name=DATADB.students.find({"Subject":sagan})
                for person in Name:
                    print(person)
        elif shepas!="":
                Name=DATADB.students.find({"shefaseba":int(shepas)})
                for person in Name:
                    print(person)
        else:
            print("Error occure")



    
    
    
    def Update_data(self):
        id=self.identtext.text()

        if id !="":
            type(id)
            sax=self.saxelitext.text()
            gvar=self.gvaritext.text()
            ident=self.identtext.text()
            sagan=self.saganitext.text()
            shepas=self.shepasebatext.text()
            
            if sagan!="":
                DATADB.students.update_one({"_id":int(id)},{"$set":{"Subject":sagan }})
            else:
                sagan=False
                
            if sax!="":
                DATADB.students.update_one({"_id":int(id)},{"$set":{"first_name":sax }})
            else:
                sax=False
            if gvar!="":
                DATADB.students.update_one({"_id":int(id)},{"$set":{"last_name":gvar }})
            else:
                gvar=False
            if shepas!="":
                DATADB.students.update_one({"_id":int(id)},{"$set":{"shefaseba":int(shepas) }})
            else:
                shepas=False
            
         
        else:
            print("Please enter ID")

    def DATABASE_UPLOAD(self):
        MONGODBSAGAMOCDO.create_doc()
        self.yvelachanawb.setText("Database has been uploaded!")
        self.yvelachanawb.setEnabled(False)
    
    def delete_doc(self):
        id=self.identtext.text()
        if id!="":
            DATADB.students.delete_one({"_id":int(id)})
        else:
         print("Please enter id")
    def insert_doc(self):
        
        id=self.identtext.text()
        if id!="":
            
            checkid=DATADB.students.find({"_id":int(id)})
            for i in checkid:
                print(i)
                if i=="":
                    id=i
                else:
                    print("ID already registered")
        

           
        else:
            print("Please enter ID")
        sax=self.saxelitext.text()
        gvar=self.gvaritext.text()
        ident=self.identtext.text()
        sagan=self.saganitext.text()
        shepas=self.shepasebatext.text()
            
        if sagan!="":
                sagan=self.saganitext.text()
        else:
                sagan=False
                
        if sax!="":
                sax=self.saxelitext.text()
        else:
                sax=False
        if gvar!="":
                gvar=self.gvaritext.text()
        else:
                gvar=False
        if shepas!="":
                shepas=self.shepasebatext.text()
        else:
                shepas=False
        newdoc={"_id":int(id),"first_name":sax,"last_name":gvar,"Subject":sagan,"Point":int(shepas)}
        DATADB.students.insert_one(newdoc)
        find=DATADB.students.find({"_id":int(id)})
        for k in find:
            print("New Data",k)
    def close(self):
        conn.drop_database('UNIVERSITY')
        MainWindow.close()
        print("***********************CAUTION*******************************DATABASE 'UNIVERSITY' was deleted****************************CAUTION*****************************")





        
        

    
    
    


        
        
        
        
        
    
    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





