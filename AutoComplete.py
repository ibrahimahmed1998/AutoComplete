from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType    # False Err
import sqlite3
import sys
################################################
FORM_CLASS,_ = loadUiType("AutoComp.ui")    # Don't Edit Here
NameList = [] # Array To Get All Names From SQLITE_DB
################################################
class MainWindow(QMainWindow,FORM_CLASS):       ############
    def __init__(self):                         #   Stamp  #
        QMainWindow.__init__(self)              #          #
        self.setupUi(self)                      ############
        self.db()
        self.LineEdit()
        self.setWindowTitle("Auto Complete")
################################################
    def db(self):   # Database Connection #
        self.connection = sqlite3.connect("db_file.db")
        names = self.connection.execute("SELECT * FROM names")
        for name in names:
           NameList.append(name[1])
################################################
    def LineEdit(self): # Prepare Model To Pass it To Auto Complete Function #
        NameLine_Edit = self.lineEdit
        Completer = QCompleter()
        NameLine_Edit.setCompleter(Completer)
        model = QStringListModel()
        Completer.setModel(model)
        self.Auto_Compelete(model)
################################################
    def Auto_Compelete(self, model):  # Put Model To Pass NameList To It #
        model.setStringList(NameList)
################################################
def main():
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec_()
################################################
if __name__=='__main__':
    main()
